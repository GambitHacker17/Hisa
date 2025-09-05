import asyncio 
import inspect 
import itertools 
import typing 
import warnings 

from ..import helpers ,utils ,errors ,hints ,events ,extensions 
from ..requestiter import RequestIter 
from ..tl import types ,functions 

_MAX_CHUNK_SIZE =100 

if typing .TYPE_CHECKING :
    from .telegramclient import TelegramClient 

class _MessagesIter (RequestIter ):
    """"""
    async def _init (
    self ,entity ,offset_id ,min_id ,max_id ,
    from_user ,offset_date ,add_offset ,filter ,search ,reply_to ,
    scheduled 
    ):

        if entity :
            self .entity =await self .client .get_input_entity (entity )
        else :
            self .entity =None 
            if self .reverse :
                raise ValueError ('Cannot reverse global search')

        if self .reverse :
            offset_id =max (offset_id ,min_id )
            if offset_id and max_id :
                if max_id -offset_id <=1 :
                    raise StopAsyncIteration 

            if not max_id :
                max_id =float ('inf')
        else :
            offset_id =max (offset_id ,max_id )
            if offset_id and min_id :
                if offset_id -min_id <=1 :
                    raise StopAsyncIteration 

        if self .reverse :
            if offset_id :
                offset_id +=1 
            elif not offset_date :

                offset_id =1 

        if from_user :
            from_user =await self .client .get_input_entity (from_user )
            self .from_id =await self .client .get_peer_id (from_user )
        else :
            self .from_id =None 

        if not self .entity and from_user :
            self .entity =types .InputPeerEmpty ()

        if filter is None :
            filter =types .InputMessagesFilterEmpty ()
        else :
            filter =filter ()if isinstance (filter ,type )else filter 

        if not self .entity :
            self .request =functions .messages .SearchGlobalRequest (
            q =search or '',
            filter =filter ,
            min_date =None ,
            max_date =offset_date ,
            offset_rate =0 ,
            offset_peer =types .InputPeerEmpty (),
            offset_id =offset_id ,
            limit =1 
            )
        elif scheduled :
            self .request =functions .messages .GetScheduledHistoryRequest (
            peer =entity ,
            hash =0 
            )
        elif reply_to is not None :
            self .request =functions .messages .GetRepliesRequest (
            peer =self .entity ,
            msg_id =reply_to ,
            offset_id =offset_id ,
            offset_date =offset_date ,
            add_offset =add_offset ,
            limit =1 ,
            max_id =0 ,
            min_id =0 ,
            hash =0 
            )
        elif search is not None or not isinstance (filter ,types .InputMessagesFilterEmpty )or from_user :

            ty =helpers ._entity_type (self .entity )
            if ty ==helpers ._EntityType .USER :

                from_user =None 
            else :

                self .from_id =None 

            self .request =functions .messages .SearchRequest (
            peer =self .entity ,
            q =search or '',
            filter =filter ,
            min_date =None ,
            max_date =offset_date ,
            offset_id =offset_id ,
            add_offset =add_offset ,
            limit =0 ,
            max_id =0 ,
            min_id =0 ,
            hash =0 ,
            from_id =from_user 
            )

            if not isinstance (filter ,types .InputMessagesFilterEmpty )and offset_date and not search and not offset_id :
                async for m in self .client .iter_messages (
                self .entity ,1 ,offset_date =offset_date ):
                    self .request .offset_id =m .id +1 
        else :
            self .request =functions .messages .GetHistoryRequest (
            peer =self .entity ,
            limit =1 ,
            offset_date =offset_date ,
            offset_id =offset_id ,
            min_id =0 ,
            max_id =0 ,
            add_offset =add_offset ,
            hash =0 
            )

        if self .limit <=0 :

            result =await self .client (self .request )
            if isinstance (result ,types .messages .MessagesNotModified ):
                self .total =result .count 
            else :
                self .total =getattr (result ,'count',len (result .messages ))
            raise StopAsyncIteration 

        if self .wait_time is None :
            self .wait_time =1 if self .limit >3000 else 0 

        if self .reverse :
            self .request .add_offset -=_MAX_CHUNK_SIZE 

        self .add_offset =add_offset 
        self .max_id =max_id 
        self .min_id =min_id 
        self .last_id =0 if self .reverse else float ('inf')

    async def _load_next_chunk (self ):
        self .request .limit =min (self .left ,_MAX_CHUNK_SIZE )
        if self .reverse and self .request .limit !=_MAX_CHUNK_SIZE :

            self .request .add_offset =self .add_offset -self .request .limit 

        r =await self .client (self .request )
        self .total =getattr (r ,'count',len (r .messages ))

        entities ={utils .get_peer_id (x ):x 
        for x in itertools .chain (r .users ,r .chats )}

        messages =reversed (r .messages )if self .reverse else r .messages 
        for message in messages :
            if (isinstance (message ,types .MessageEmpty )
            or self .from_id and message .sender_id !=self .from_id ):
                continue 

            if not self ._message_in_range (message ):
                return True 

            self .last_id =message .id 
            message ._finish_init (self .client ,entities ,self .entity )
            self .buffer .append (message )

        if isinstance (r ,types .messages .Messages ):
            return True 

        if not r .messages or r .messages [0 ].id <=self .request .limit :
            return True 

        if self .buffer :
            self ._update_offset (self .buffer [-1 ],r )
        else :

            return True 

    def _message_in_range (self ,message ):
        """"""

        if self .entity :
            if self .reverse :
                if message .id <=self .last_id or message .id >=self .max_id :
                    return False 
            else :
                if message .id >=self .last_id or message .id <=self .min_id :
                    return False 

        return True 

    def _update_offset (self ,last_message ,response ):
        """"""
        self .request .offset_id =last_message .id 
        if self .reverse :

            self .request .offset_id +=1 

        if isinstance (self .request ,functions .messages .SearchRequest ):

            self .request .max_date =None 
        else :

            self .request .offset_date =last_message .date 

        if isinstance (self .request ,functions .messages .SearchGlobalRequest ):
            if last_message .input_chat :
                self .request .offset_peer =last_message .input_chat 
            else :
                self .request .offset_peer =types .InputPeerEmpty ()

            self .request .offset_rate =getattr (response ,'next_rate',0 )

class _IDsIter (RequestIter ):
    async def _init (self ,entity ,ids ):
        self .total =len (ids )
        self ._ids =list (reversed (ids ))if self .reverse else ids 
        self ._offset =0 
        self ._entity =(await self .client .get_input_entity (entity ))if entity else None 
        self ._ty =helpers ._entity_type (self ._entity )if self ._entity else None 

        if self .wait_time is None :
            self .wait_time =10 if self .limit >300 else 0 

    async def _load_next_chunk (self ):
        ids =self ._ids [self ._offset :self ._offset +_MAX_CHUNK_SIZE ]
        if not ids :
            raise StopAsyncIteration 

        self ._offset +=_MAX_CHUNK_SIZE 

        from_id =None 
        if self ._ty ==helpers ._EntityType .CHANNEL :
            try :
                r =await self .client (
                functions .channels .GetMessagesRequest (self ._entity ,ids ))
            except errors .MessageIdsEmptyError :

                r =types .messages .MessagesNotModified (len (ids ))
        else :
            r =await self .client (functions .messages .GetMessagesRequest (ids ))
            if self ._entity :
                from_id =await self .client ._get_peer (self ._entity )

        if isinstance (r ,types .messages .MessagesNotModified ):
            self .buffer .extend (None for _ in ids )
            return 

        entities ={utils .get_peer_id (x ):x 
        for x in itertools .chain (r .users ,r .chats )}

        for message in r .messages :
            if isinstance (message ,types .MessageEmpty )or (
            from_id and message .peer_id !=from_id ):
                self .buffer .append (None )
            else :
                message ._finish_init (self .client ,entities ,self ._entity )
                self .buffer .append (message )

class MessageMethods :

    def iter_messages (
    self :'TelegramClient',
    entity :'hints.EntityLike',
    limit :float =None ,
    *,
    offset_date :'hints.DateLike'=None ,
    offset_id :int =0 ,
    max_id :int =0 ,
    min_id :int =0 ,
    add_offset :int =0 ,
    search :str =None ,
    filter :'typing.Union[types.TypeMessagesFilter, typing.Type[types.TypeMessagesFilter]]'=None ,
    from_user :'hints.EntityLike'=None ,
    wait_time :float =None ,
    ids :'typing.Union[int, typing.Sequence[int]]'=None ,
    reverse :bool =False ,
    reply_to :int =None ,
    scheduled :bool =False 
    )->'typing.Union[_MessagesIter, _IDsIter]':
        """"""
        if ids is not None :
            if not utils .is_list_like (ids ):
                ids =[ids ]

            return _IDsIter (
            client =self ,
            reverse =reverse ,
            wait_time =wait_time ,
            limit =len (ids ),
            entity =entity ,
            ids =ids 
            )

        return _MessagesIter (
        client =self ,
        reverse =reverse ,
        wait_time =wait_time ,
        limit =limit ,
        entity =entity ,
        offset_id =offset_id ,
        min_id =min_id ,
        max_id =max_id ,
        from_user =from_user ,
        offset_date =offset_date ,
        add_offset =add_offset ,
        filter =filter ,
        search =search ,
        reply_to =reply_to ,
        scheduled =scheduled 
        )

    async def get_messages (self :'TelegramClient',*args ,**kwargs )->'hints.TotalList':
        """"""
        if len (args )==1 and 'limit'not in kwargs :
            if 'min_id'in kwargs and 'max_id'in kwargs :
                kwargs ['limit']=None 
            else :
                kwargs ['limit']=1 

        it =self .iter_messages (*args ,**kwargs )

        ids =kwargs .get ('ids')
        if ids and not utils .is_list_like (ids ):
            async for message in it :
                return message 
            else :

                return None 

        return await it .collect ()

    get_messages .__signature__ =inspect .signature (iter_messages )

    async def _get_comment_data (
    self :'TelegramClient',
    entity :'hints.EntityLike',
    message :'typing.Union[int, types.Message]'
    ):
        r =await self (functions .messages .GetDiscussionMessageRequest (
        peer =entity ,
        msg_id =utils .get_message_id (message )
        ))
        m =min (r .messages ,key =lambda msg :msg .id )
        chat =next (c for c in r .chats if c .id ==m .peer_id .channel_id )
        return utils .get_input_peer (chat ),m .id 

    async def send_message (
    self :'TelegramClient',
    entity :'hints.EntityLike',
    message :'hints.MessageLike'='',
    *,
    top_msg_id :int =None ,
    reply_to :'typing.Union[int, types.Message, types.StoryItem, types.TypeInputReplyTo]'=None ,
    attributes :'typing.Sequence[types.TypeDocumentAttribute]'=None ,
    parse_mode :typing .Optional [str ]=(),
    formatting_entities :typing .Optional [typing .List [types .TypeMessageEntity ]]=None ,
    link_preview :bool =True ,
    file :'typing.Union[hints.FileLike, typing.Sequence[hints.FileLike]]'=None ,
    thumb :'hints.FileLike'=None ,
    force_document :bool =False ,
    clear_draft :bool =False ,
    buttons :typing .Optional ['hints.MarkupLike']=None ,
    silent :bool =None ,
    background :bool =None ,
    supports_streaming :bool =False ,
    schedule :'hints.DateLike'=None ,
    comment_to :'typing.Union[int, types.Message]'=None ,
    nosound_video :bool =None 
    )->'types.Message':
        """"""
        if file is not None :
            return await self .send_file (
            entity ,file ,caption =message ,reply_to =reply_to ,
            top_msg_id =top_msg_id ,
            attributes =attributes ,parse_mode =parse_mode ,
            force_document =force_document ,thumb =thumb ,
            buttons =buttons ,clear_draft =clear_draft ,silent =silent ,
            schedule =schedule ,supports_streaming =supports_streaming ,
            formatting_entities =formatting_entities ,
            comment_to =comment_to ,background =background ,
            nosound_video =nosound_video 
            )

        entity =await self .get_input_entity (entity )
        if comment_to is not None :
            entity ,reply_to =await self ._get_comment_data (entity ,comment_to )

        reply_to =utils .get_input_reply_to (entity ,reply_to ,top_msg_id )

        if isinstance (message ,types .Message ):
            if buttons is None :
                markup =message .reply_markup 
            else :
                markup =self .build_reply_markup (buttons )

            if silent is None :
                silent =message .silent 

            if (message .media and not isinstance (
            message .media ,types .MessageMediaWebPage )):
                return await self .send_file (
                entity ,
                message .media ,
                caption =message .message ,
                top_msg_id =top_msg_id ,
                silent =silent ,
                background =background ,
                reply_to =reply_to ,
                buttons =markup ,
                formatting_entities =message .entities ,
                parse_mode =None ,
                schedule =schedule 
                )

            request =functions .messages .SendMessageRequest (
            peer =entity ,
            message =message .message or '',
            silent =silent ,
            background =background ,
            reply_to =reply_to ,
            reply_markup =markup ,
            entities =message .entities ,
            clear_draft =clear_draft ,
            no_webpage =not isinstance (
            message .media ,types .MessageMediaWebPage ),
            schedule_date =schedule 
            )
            message =message .message 
        else :
            if formatting_entities is None :
                message ,formatting_entities =await self ._parse_message_text (message ,parse_mode )
            if not message :
                raise ValueError (
                'The message cannot be empty unless a file is provided'
                )

            request =functions .messages .SendMessageRequest (
            peer =entity ,
            message =message ,
            entities =formatting_entities ,
            no_webpage =not link_preview ,
            reply_to =reply_to ,
            clear_draft =clear_draft ,
            silent =silent ,
            background =background ,
            reply_markup =self .build_reply_markup (buttons ),
            schedule_date =schedule 
            )

        result =await self (request )
        if isinstance (result ,types .UpdateShortSentMessage ):
            message =types .Message (
            id =result .id ,
            peer_id =await self ._get_peer (entity ),
            message =message ,
            date =result .date ,
            out =result .out ,
            media =result .media ,
            entities =result .entities ,
            reply_markup =request .reply_markup ,
            ttl_period =result .ttl_period ,
            reply_to =types .MessageReplyHeader (request .reply_to )
            )
            message ._finish_init (self ,{},entity )
            return message 

        return self ._get_response_message (request ,result ,entity )

    async def forward_messages (
    self :'TelegramClient',
    entity :'hints.EntityLike',
    messages :'typing.Union[hints.MessageIDLike, typing.Sequence[hints.MessageIDLike]]',
    from_peer :'hints.EntityLike'=None ,
    *,
    background :bool =None ,
    with_my_score :bool =None ,
    silent :bool =None ,
    as_album :bool =None ,
    schedule :'hints.DateLike'=None ,
    top_msg_id :int =None 
    )->'typing.Sequence[types.Message]':
        """"""
        if as_album is not None :
            warnings .warn ('the as_album argument is deprecated and no longer has any effect')

        single =not utils .is_list_like (messages )
        if single :
            messages =(messages ,)

        entity =await self .get_input_entity (entity )

        if from_peer :
            from_peer =await self .get_input_entity (from_peer )
            from_peer_id =await self .get_peer_id (from_peer )
        else :
            from_peer_id =None 

        def get_key (m ):
            if isinstance (m ,int ):
                if from_peer_id is not None :
                    return from_peer_id 

                raise ValueError ('from_peer must be given if integer IDs are used')
            elif isinstance (m ,types .Message ):
                return m .chat_id 
            else :
                raise TypeError ('Cannot forward messages of type {}'.format (type (m )))

        sent =[]
        for _chat_id ,chunk in itertools .groupby (messages ,key =get_key ):
            chunk =list (chunk )
            if isinstance (chunk [0 ],int ):
                chat =from_peer 
            else :
                chat =from_peer or await self .get_input_entity (chunk [0 ].peer_id )
                chunk =[m .id for m in chunk ]

            req =functions .messages .ForwardMessagesRequest (
            from_peer =chat ,
            id =chunk ,
            to_peer =entity ,
            silent =silent ,
            background =background ,
            with_my_score =with_my_score ,
            schedule_date =schedule ,
            top_msg_id =top_msg_id 
            )
            result =await self (req )
            sent .extend (self ._get_response_message (req ,result ,entity ))

        return sent [0 ]if single else sent 

    async def edit_message (
    self :'TelegramClient',
    entity :'typing.Union[hints.EntityLike, types.Message]',
    message :'hints.MessageLike'=None ,
    text :str =None ,
    *,
    parse_mode :str =(),
    attributes :'typing.Sequence[types.TypeDocumentAttribute]'=None ,
    formatting_entities :typing .Optional [typing .List [types .TypeMessageEntity ]]=None ,
    link_preview :bool =True ,
    file :'hints.FileLike'=None ,
    thumb :'hints.FileLike'=None ,
    force_document :bool =False ,
    buttons :typing .Optional ['hints.MarkupLike']=None ,
    supports_streaming :bool =False ,
    schedule :'hints.DateLike'=None 
    )->'types.Message':
        """"""
        if isinstance (entity ,types .InputBotInlineMessageID ):
            text =text or message 
            message =entity 
        elif isinstance (entity ,types .Message ):
            text =message 
            message =entity 
            entity =entity .peer_id 

        if formatting_entities is None :
            text ,formatting_entities =await self ._parse_message_text (text ,parse_mode )
        file_handle ,media ,image =await self ._file_to_media (file ,
        supports_streaming =supports_streaming ,
        thumb =thumb ,
        attributes =attributes ,
        force_document =force_document )

        if isinstance (entity ,types .InputBotInlineMessageID ):
            request =functions .messages .EditInlineBotMessageRequest (
            id =entity ,
            message =text ,
            no_webpage =not link_preview ,
            entities =formatting_entities ,
            media =media ,
            reply_markup =self .build_reply_markup (buttons )
            )

            exported =self .session .dc_id !=entity .dc_id 
            if exported :
                try :
                    sender =await self ._borrow_exported_sender (entity .dc_id )
                    return await self ._call (sender ,request )
                finally :
                    await self ._return_exported_sender (sender )
            else :
                return await self (request )

        entity =await self .get_input_entity (entity )
        request =functions .messages .EditMessageRequest (
        peer =entity ,
        id =utils .get_message_id (message ),
        message =text ,
        no_webpage =not link_preview ,
        entities =formatting_entities ,
        media =media ,
        reply_markup =self .build_reply_markup (buttons ),
        schedule_date =schedule 
        )
        msg =self ._get_response_message (request ,await self (request ),entity )
        return msg 

    async def delete_messages (
    self :'TelegramClient',
    entity :'hints.EntityLike',
    message_ids :'typing.Union[hints.MessageIDLike, typing.Sequence[hints.MessageIDLike]]',
    *,
    revoke :bool =True )->'typing.Sequence[types.messages.AffectedMessages]':
        """"""
        if not utils .is_list_like (message_ids ):
            message_ids =(message_ids ,)

        message_ids =(
        m .id if isinstance (m ,(
        types .Message ,types .MessageService ,types .MessageEmpty ))
        else int (m )for m in message_ids 
        )

        if entity :
            entity =await self .get_input_entity (entity )
            ty =helpers ._entity_type (entity )
        else :

            ty =helpers ._EntityType .USER 

        if ty ==helpers ._EntityType .CHANNEL :
            return await self ([functions .channels .DeleteMessagesRequest (
            entity ,list (c ))for c in utils .chunks (message_ids )])
        else :
            return await self ([functions .messages .DeleteMessagesRequest (
            list (c ),revoke )for c in utils .chunks (message_ids )])

    async def send_read_acknowledge (
    self :'TelegramClient',
    entity :'hints.EntityLike',
    message :'typing.Union[hints.MessageIDLike, typing.Sequence[hints.MessageIDLike]]'=None ,
    *,
    max_id :int =None ,
    clear_mentions :bool =False ,
    clear_reactions :bool =False ,
    top_msg_id :int =None )->bool :
        """"""
        if max_id is None :
            if not message :
                max_id =0 
            else :
                if utils .is_list_like (message ):
                    max_id =max (msg .id for msg in message )
                else :
                    max_id =message .id 

        entity =await self .get_input_entity (entity )
        if clear_mentions :
            await self (functions .messages .ReadMentionsRequest (entity ,top_msg_id ))
            if max_id is None and not clear_reactions :
                return True 
        if clear_reactions :
            await self (functions .messages .ReadReactionsRequest (entity ,top_msg_id ))
            if max_id is None :
                return True 

        if max_id is not None :
            if helpers ._entity_type (entity )==helpers ._EntityType .CHANNEL :
                return await self (functions .channels .ReadHistoryRequest (
                utils .get_input_channel (entity ),max_id =max_id ))
            else :
                return await self (functions .messages .ReadHistoryRequest (
                entity ,max_id =max_id ))

        return False 

    async def pin_message (
    self :'TelegramClient',
    entity :'hints.EntityLike',
    message :'typing.Optional[hints.MessageIDLike]',
    *,
    notify :bool =False ,
    pm_oneside :bool =False 
    ):
        """"""
        return await self ._pin (entity ,message ,unpin =False ,notify =notify ,pm_oneside =pm_oneside )

    async def unpin_message (
    self :'TelegramClient',
    entity :'hints.EntityLike',
    message :'typing.Optional[hints.MessageIDLike]'=None ,
    *,
    notify :bool =False 
    ):
        """"""
        return await self ._pin (entity ,message ,unpin =True ,notify =notify )

    async def _pin (self ,entity ,message ,*,unpin ,notify =False ,pm_oneside =False ):
        message =utils .get_message_id (message )or 0 
        entity =await self .get_input_entity (entity )
        if message <=0 :
            await self (functions .messages .UnpinAllMessagesRequest (entity ))
            return 

        request =functions .messages .UpdatePinnedMessageRequest (
        peer =entity ,
        id =message ,
        silent =not notify ,
        unpin =unpin ,
        pm_oneside =pm_oneside 
        )
        result =await self (request )

        if unpin or not result .updates :
            return 

        return self ._get_response_message (request ,result ,entity )

    async def report_reaction (
    self :"TelegramClient",
    peer :"hints.EntityLike",
    id :int ,
    reaction_peer :"hints.EntityLike",
    )->bool :
        return await self (
        functions .messages .ReportReactionRequest (peer ,id ,reaction_peer )
        )

    async def send_reaction (
    self :"TelegramClient",
    entity :"hints.DialogLike",
    message :"hints.MessageIDLike",
    reaction :"typing.Optional[hints.Reaction]"=None ,
    big :bool =False ,
    add_to_recent :bool =False ,
    ):
        reaction =utils .convert_reaction (reaction )
        message =utils .get_message_id (message )or 0 
        if not reaction :
            get_default_request =functions .help .GetAppConfigRequest ()
            app_config =await self (get_default_request )
            reaction =(
            next ((y for y in app_config .value if "reactions_default"in y .key ))
            ).value .value 

        request =functions .messages .SendReactionRequest (
        big =big ,
        peer =entity ,
        msg_id =message ,
        reaction =reaction ,
        add_to_recent =add_to_recent ,
        )
        result =await self (request )
        for update in result .updates :
            if isinstance (update ,types .UpdateMessageReactions ):
                return update .reactions 
            if isinstance (update ,types .UpdateEditMessage ):
                return update .message .reactions 

    async def set_quick_reaction (self :"TelegramClient",reaction :"hints.Reaction"):
        request =functions .messages .SetDefaultReactionRequest (
        reaction =utils .convert_reaction (reaction )
        )
        return await self (request )

    async def transcribe (
    self :"TelegramClient",
    peer :"hints.EntityLike",
    message :"hints.MessageIDLike",
    timeout :int =15 ,
    )->typing .Optional [str ]:
        result =await self (
        functions .messages .TranscribeAudioRequest (
        peer ,
        utils .get_message_id (message ),
        )
        )

        transcription_result =None 

        event =asyncio .Event ()

        @self .on (events .Raw (types .UpdateTranscribedAudio ))
        async def handler (update ):
            nonlocal result ,transcription_result 
            if update .transcription_id !=result .transcription_id or update .pending :
                return 

            transcription_result =update .text 
            event .set ()
            raise events .StopPropagation 

        try :
            await asyncio .wait_for (event .wait (),timeout =timeout )
        except Exception :
            return None 

        return transcription_result 

    async def translate (
    self :"TelegramClient",
    peer :"hints.EntityLike",
    message :"hints.MessageIDLike",
    to_lang :str ,
    raw_text :"typing.Optional[str]"=None ,
    entities :"typing.Optional[typing.List[types.MessageEntity]]"=None ,
    )->str :
        msg_id =utils .get_message_id (message )or 0 
        if not msg_id :
            return None 

        if not isinstance (message ,types .Message ):
            message =(await self .get_messages (peer ,ids =[msg_id ]))[0 ]

        result =await self (
        functions .messages .TranslateTextRequest (
        peer =peer ,
        id =[msg_id ],
        text =[
        types .TextWithEntities (
        raw_text or message .raw_text ,
        entities or message .entities or [],
        )
        ],
        to_lang =to_lang ,
        )
        )

        return (
        extensions .html .unparse (
        result .result [0 ].text ,
        result .result [0 ].entities ,
        )
        if result and result .result 
        else ""
        )

