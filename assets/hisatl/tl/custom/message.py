from typing import Optional ,List ,TYPE_CHECKING 
from datetime import datetime 
from .chatgetter import ChatGetter 
from .sendergetter import SenderGetter 
from .messagebutton import MessageButton 
from .forward import Forward 
from .file import File 
from ..import TLObject ,types ,functions ,alltlobjects 
from ...import utils ,errors 

class Message (ChatGetter ,SenderGetter ,TLObject ):
    """"""

    def __init__ (

    self ,id :int ,

    peer_id :types .TypePeer =None ,
    date :Optional [datetime ]=None ,

    out :Optional [bool ]=None ,
    mentioned :Optional [bool ]=None ,
    media_unread :Optional [bool ]=None ,
    silent :Optional [bool ]=None ,
    post :Optional [bool ]=None ,
    from_id :Optional [types .TypePeer ]=None ,
    reply_to :Optional [types .TypeMessageReplyHeader ]=None ,
    ttl_period :Optional [int ]=None ,

    message :Optional [str ]=None ,

    fwd_from :Optional [types .TypeMessageFwdHeader ]=None ,
    via_bot_id :Optional [int ]=None ,
    media :Optional [types .TypeMessageMedia ]=None ,
    reply_markup :Optional [types .TypeReplyMarkup ]=None ,
    entities :Optional [List [types .TypeMessageEntity ]]=None ,
    views :Optional [int ]=None ,
    edit_date :Optional [datetime ]=None ,
    post_author :Optional [str ]=None ,
    grouped_id :Optional [int ]=None ,
    from_scheduled :Optional [bool ]=None ,
    legacy :Optional [bool ]=None ,
    edit_hide :Optional [bool ]=None ,
    pinned :Optional [bool ]=None ,
    noforwards :Optional [bool ]=None ,
    reactions :Optional [types .TypeMessageReactions ]=None ,
    restriction_reason :Optional [types .TypeRestrictionReason ]=None ,
    forwards :Optional [int ]=None ,
    replies :Optional [types .TypeMessageReplies ]=None ,
    invert_media :Optional [bool ]=None ,

    action :Optional [types .TypeMessageAction ]=None 
    ):

        self .out =bool (out )
        self .invert_media =bool (invert_media )
        self .mentioned =mentioned 
        self .media_unread =media_unread 
        self .silent =silent 
        self .post =post 
        self .from_scheduled =from_scheduled 
        self .legacy =legacy 
        self .edit_hide =edit_hide 
        self .id =id 
        self .from_id =from_id 
        self .peer_id =peer_id 
        self .fwd_from =fwd_from 
        self .via_bot_id =via_bot_id 
        self .reply_to =reply_to 
        self .date =date 
        self .message =message 
        self .media =None if isinstance (media ,types .MessageMediaEmpty )else media 
        self .reply_markup =reply_markup 
        self .entities =entities 
        self .views =views 
        self .forwards =forwards 
        self .replies =replies 
        self .edit_date =edit_date 
        self .pinned =pinned 
        self .noforwards =noforwards 
        self .post_author =post_author 
        self .grouped_id =grouped_id 
        self .reactions =reactions 
        self .restriction_reason =restriction_reason 
        self .ttl_period =ttl_period 
        self .action =action 

        self ._client =None 
        self ._text =None 
        self ._file =None 
        self ._reply_message =None 
        self ._buttons =None 
        self ._buttons_flat =None 
        self ._buttons_count =None 
        self ._via_bot =None 
        self ._via_input_bot =None 
        self ._action_entities =None 
        self ._linked_chat =None 

        sender_id =None 
        if from_id is not None :
            sender_id =utils .get_peer_id (from_id )
        elif peer_id :

            if post or (not out and isinstance (peer_id ,types .PeerUser )):
                sender_id =utils .get_peer_id (peer_id )

        self .old_from_id =self .from_id 
        self .from_id =sender_id 

        ChatGetter .__init__ (self ,peer_id ,broadcast =post )
        SenderGetter .__init__ (self ,sender_id )

        self ._forward =None 

    def _finish_init (self ,client ,entities ,input_chat ):
        """"""
        self ._client =client 

        if self .peer_id ==types .PeerUser (client ._self_id )and not self .fwd_from :
            self .out =True 

        cache =client ._entity_cache 

        self ._sender ,self ._input_sender =utils ._get_entity_pair (
        self .sender_id ,entities ,cache )

        self ._chat ,self ._input_chat =utils ._get_entity_pair (
        self .chat_id ,entities ,cache )

        if input_chat :
            self ._input_chat =input_chat 

        if self .via_bot_id :
            self ._via_bot ,self ._via_input_bot =utils ._get_entity_pair (
            self .via_bot_id ,entities ,cache )

        if self .fwd_from :
            self ._forward =Forward (self ._client ,self .fwd_from ,entities )

        if self .action :
            if isinstance (self .action ,(types .MessageActionChatAddUser ,
            types .MessageActionChatCreate )):
                self ._action_entities =[entities .get (i )
                for i in self .action .users ]
            elif isinstance (self .action ,types .MessageActionChatDeleteUser ):
                self ._action_entities =[entities .get (self .action .user_id )]
            elif isinstance (self .action ,types .MessageActionChatJoinedByLink ):
                self ._action_entities =[entities .get (self .action .inviter_id )]
            elif isinstance (self .action ,types .MessageActionChatMigrateTo ):
                self ._action_entities =[entities .get (utils .get_peer_id (
                types .PeerChannel (self .action .channel_id )))]
            elif isinstance (
            self .action ,types .MessageActionChannelMigrateFrom ):
                self ._action_entities =[entities .get (utils .get_peer_id (
                types .PeerChat (self .action .chat_id )))]

        if self .replies and self .replies .channel_id :
            self ._linked_chat =entities .get (utils .get_peer_id (
            types .PeerChannel (self .replies .channel_id )))

    @property 
    def client (self ):
        """"""
        return self ._client 

    @property 
    def text (self ):
        """"""
        if self ._text is None and self ._client :
            if not self ._client .parse_mode :
                self ._text =self .message 
            else :
                self ._text =self ._client .parse_mode .unparse (
                self .message ,self .entities )

        return self ._text 

    @text .setter 
    def text (self ,value ):
        self ._text =value 
        if self ._client and self ._client .parse_mode :
            self .message ,self .entities =self ._client .parse_mode .parse (value )
        else :
            self .message ,self .entities =value ,[]

    @property 
    def raw_text (self ):
        """"""
        return self .message 

    @raw_text .setter 
    def raw_text (self ,value ):
        self .message =value 
        self .entities =[]
        self ._text =None 

    @property 
    def is_reply (self ):
        """"""
        return self .reply_to is not None 

    @property 
    def forward (self ):
        """"""
        return self ._forward 

    @property 
    def buttons (self ):
        """"""
        if self ._buttons is None and self .reply_markup :
            if not self .input_chat :
                return 
            try :
                bot =self ._needed_markup_bot ()
            except ValueError :
                return 
            else :
                self ._set_buttons (self ._input_chat ,bot )

        return self ._buttons 

    async def get_buttons (self ):
        """"""
        if not self .buttons and self .reply_markup :
            chat =await self .get_input_chat ()
            if not chat :
                return 
            try :
                bot =self ._needed_markup_bot ()
            except ValueError :
                await self ._reload_message ()
                bot =self ._needed_markup_bot ()

            self ._set_buttons (chat ,bot )

        return self ._buttons 

    @property 
    def button_count (self ):
        """"""
        if self ._buttons_count is None :
            if isinstance (self .reply_markup ,(
            types .ReplyInlineMarkup ,types .ReplyKeyboardMarkup )):
                self ._buttons_count =sum (
                len (row .buttons )for row in self .reply_markup .rows )
            else :
                self ._buttons_count =0 

        return self ._buttons_count 

    @property 
    def file (self ):
        """"""
        if not self ._file :
            media =self .photo or self .document 
            if media :
                self ._file =File (media )

        return self ._file 

    @property 
    def photo (self ):
        """"""
        if isinstance (self .media ,types .MessageMediaPhoto ):
            if isinstance (self .media .photo ,types .Photo ):
                return self .media .photo 
        elif isinstance (self .action ,types .MessageActionChatEditPhoto ):
            return self .action .photo 
        else :
            web =self .web_preview 
            if web and isinstance (web .photo ,types .Photo ):
                return web .photo 

    @property 
    def document (self ):
        """"""
        if isinstance (self .media ,types .MessageMediaDocument ):
            if isinstance (self .media .document ,types .Document ):
                return self .media .document 
        else :
            web =self .web_preview 
            if web and isinstance (web .document ,types .Document ):
                return web .document 

    @property 
    def web_preview (self ):
        """"""
        if isinstance (self .media ,types .MessageMediaWebPage ):
            if isinstance (self .media .webpage ,types .WebPage ):
                return self .media .webpage 

    @property 
    def audio (self ):
        """"""
        return self ._document_by_attribute (types .DocumentAttributeAudio ,
        lambda attr :not attr .voice )

    @property 
    def voice (self ):
        """"""
        return self ._document_by_attribute (types .DocumentAttributeAudio ,
        lambda attr :attr .voice )

    @property 
    def video (self ):
        """"""
        return self ._document_by_attribute (types .DocumentAttributeVideo )

    @property 
    def video_note (self ):
        """"""
        return self ._document_by_attribute (types .DocumentAttributeVideo ,
        lambda attr :attr .round_message )

    @property 
    def gif (self ):
        """"""
        return self ._document_by_attribute (types .DocumentAttributeAnimated )

    @property 
    def sticker (self ):
        """"""
        return self ._document_by_attribute (types .DocumentAttributeSticker )

    @property 
    def contact (self ):
        """"""
        if isinstance (self .media ,types .MessageMediaContact ):
            return self .media 

    @property 
    def game (self ):
        """"""
        if isinstance (self .media ,types .MessageMediaGame ):
            return self .media .game 

    @property 
    def geo (self ):
        """"""
        if isinstance (self .media ,(types .MessageMediaGeo ,
        types .MessageMediaGeoLive ,
        types .MessageMediaVenue )):
            return self .media .geo 

    @property 
    def invoice (self ):
        """"""
        if isinstance (self .media ,types .MessageMediaInvoice ):
            return self .media 

    @property 
    def poll (self ):
        """"""
        if isinstance (self .media ,types .MessageMediaPoll ):
            return self .media 

    @property 
    def venue (self ):
        """"""
        if isinstance (self .media ,types .MessageMediaVenue ):
            return self .media 

    @property 
    def dice (self ):
        """"""
        if isinstance (self .media ,types .MessageMediaDice ):
            return self .media 

    @property 
    def action_entities (self ):
        """"""
        return self ._action_entities 

    @property 
    def via_bot (self ):
        """"""
        return self ._via_bot 

    @property 
    def via_input_bot (self ):
        """"""
        return self ._via_input_bot 

    @property 
    def reply_to_msg_id (self ):
        """"""
        return self .reply_to .reply_to_msg_id if self .reply_to else None 

    @property 
    def to_id (self ):
        """"""

        if self ._client and not self .out and self .is_private :
            return types .PeerUser (self ._client ._self_id )

        return self .peer_id 

    def get_entities_text (self ,cls =None ):
        """"""
        ent =self .entities 
        if not ent :
            return []

        if cls :
            ent =[c for c in ent if isinstance (c ,cls )]

        texts =utils .get_inner_text (self .message ,ent )
        return list (zip (ent ,texts ))

    async def get_reply_message (self ):
        """"""
        if self ._reply_message is None and self ._client :
            if not self .reply_to :
                return None 

            self ._reply_message =await self ._client .get_messages (
            await self .get_input_chat ()if self .is_channel else None ,
            ids =types .InputMessageReplyTo (self .id )
            )
            if not self ._reply_message :

                self ._reply_message =await self ._client .get_messages (
                self ._input_chat if self .is_channel else None ,
                ids =self .reply_to .reply_to_msg_id 
                )

        return self ._reply_message 

    async def respond (self ,*args ,**kwargs ):
        """"""
        if self ._client :
            return await self ._client .send_message (
            await self .get_input_chat (),*args ,**kwargs )

    async def reply (self ,*args ,**kwargs ):
        """"""
        if self ._client :
            kwargs ['reply_to']=self .id 
            return await self ._client .send_message (
            await self .get_input_chat (),*args ,**kwargs )

    async def forward_to (self ,*args ,**kwargs ):
        """"""
        if self ._client :
            kwargs ['messages']=self .id 
            kwargs ['from_peer']=await self .get_input_chat ()
            return await self ._client .forward_messages (*args ,**kwargs )

    async def edit (self ,*args ,**kwargs ):
        """"""
        if self .fwd_from or not self .out or not self ._client :
            return None 

        if 'link_preview'not in kwargs :
            kwargs ['link_preview']=bool (self .web_preview )

        if 'buttons'not in kwargs :
            kwargs ['buttons']=self .reply_markup 

        return await self ._client .edit_message (
        await self .get_input_chat (),self .id ,
        *args ,**kwargs 
        )

    async def delete (self ,*args ,**kwargs ):
        """"""
        if self ._client :
            return await self ._client .delete_messages (
            await self .get_input_chat (),[self .id ],
            *args ,**kwargs 
            )

    async def download_media (self ,*args ,**kwargs ):
        """"""
        if self ._client :

            return await self ._client .download_media (self ,*args ,**kwargs )

    async def click (self ,i =None ,j =None ,
    *,text =None ,filter =None ,data =None ,share_phone =None ,
    share_geo =None ,password =None ):
        """"""
        if not self ._client :
            return 

        if data :
            chat =await self .get_input_chat ()
            if not chat :
                return None 

            but =types .KeyboardButtonCallback ('',data )
            return await MessageButton (self ._client ,but ,chat ,None ,self .id ).click (
            share_phone =share_phone ,share_geo =share_geo ,password =password )

        if sum (int (x is not None )for x in (i ,text ,filter ))>=2 :
            raise ValueError ('You can only set either of i, text or filter')

        if self .poll is not None :
            def find_options ():
                answers =self .poll .poll .answers 
                if i is not None :
                    if utils .is_list_like (i ):
                        return [answers [idx ].option for idx in i ]
                    return [answers [i ].option ]
                if text is not None :
                    if callable (text ):
                        for answer in answers :
                            if text (answer .text ):
                                return [answer .option ]
                    else :
                        for answer in answers :
                            if answer .text ==text :
                                return [answer .option ]
                    return 

                if filter is not None :
                    for answer in answers :
                        if filter (answer ):
                            return [answer .option ]
                    return 

            options =find_options ()
            if options is None :
                options =[]
            return await self ._client (
            functions .messages .SendVoteRequest (
            peer =self ._input_chat ,
            msg_id =self .id ,
            options =options 
            )
            )

        if not await self .get_buttons ():
            return 

        def find_button ():
            nonlocal i 
            if text is not None :
                if callable (text ):
                    for button in self ._buttons_flat :
                        if text (button .text ):
                            return button 
                else :
                    for button in self ._buttons_flat :
                        if button .text ==text :
                            return button 
                return 

            if filter is not None :
                for button in self ._buttons_flat :
                    if filter (button ):
                        return button 
                return 

            if i is None :
                i =0 
            if j is None :
                return self ._buttons_flat [i ]
            else :
                return self ._buttons [i ][j ]

        button =find_button ()
        if button :
            return await button .click (
            share_phone =share_phone ,share_geo =share_geo ,password =password )

    async def mark_read (self ):
        """"""
        if self ._client :
            await self ._client .send_read_acknowledge (
            await self .get_input_chat (),max_id =self .id )

    async def pin (self ,*,notify =False ,pm_oneside =False ):
        """"""

        if self ._client :
            return await self ._client .pin_message (
            await self .get_input_chat (),self .id ,notify =notify ,pm_oneside =pm_oneside )

    async def unpin (self ):
        """"""
        if self ._client :
            return await self ._client .unpin_message (
            await self .get_input_chat (),self .id )

    async def translate (self ,to_lang :str ):
        """"""
        if not self ._client :
            return 

        return await self ._client .translate (self .peer_id ,self ,to_lang )

    async def transcribe (self )->"typing.Optional[str]":
        """"""

        if not self ._client :
            return 

        return await self ._client .transcribe (self .peer_id ,self )

    async def react (
    self ,
    reaction :"typing.Optional[hints.Reaction]"=None ,
    big :bool =False ,
    add_to_recent :bool =False ,
    ):
        """"""
        if self ._client :
            return await self ._client .send_reaction (
            await self .get_input_chat (),
            self .id ,
            reaction ,
            big =big ,
            add_to_recent =add_to_recent ,
            )

    async def _reload_message (self ):
        """"""
        if not self ._client :
            return 

        try :
            chat =await self .get_input_chat ()if self .is_channel else None 
            msg =await self ._client .get_messages (chat ,ids =self .id )
        except ValueError :
            return 
        if not msg :
            return 

        self ._sender =msg ._sender 
        self ._input_sender =msg ._input_sender 
        self ._chat =msg ._chat 
        self ._input_chat =msg ._input_chat 
        self ._via_bot =msg ._via_bot 
        self ._via_input_bot =msg ._via_input_bot 
        self ._forward =msg ._forward 
        self ._action_entities =msg ._action_entities 

    async def _refetch_sender (self ):
        await self ._reload_message ()

    def _set_buttons (self ,chat ,bot ):
        """"""
        if self ._client and isinstance (self .reply_markup ,(
        types .ReplyInlineMarkup ,types .ReplyKeyboardMarkup )):
            self ._buttons =[[
            MessageButton (self ._client ,button ,chat ,bot ,self .id )
            for button in row .buttons 
            ]for row in self .reply_markup .rows ]
            self ._buttons_flat =[x for row in self ._buttons for x in row ]

    def _needed_markup_bot (self ):
        """"""
        if self ._client and not isinstance (self .reply_markup ,(
        types .ReplyInlineMarkup ,types .ReplyKeyboardMarkup )):
            return None 

        for row in self .reply_markup .rows :
            for button in row .buttons :
                if isinstance (button ,types .KeyboardButtonSwitchInline ):

                    if button .same_peer or not self .via_bot_id :
                        bot =self .input_sender 
                        if not bot :
                            raise ValueError ('No input sender')
                        return bot 
                    else :
                        try :
                            return self ._client ._entity_cache [self .via_bot_id ]
                        except KeyError :
                            raise ValueError ('No input sender')from None 

    def _document_by_attribute (self ,kind ,condition =None ):
        """"""
        doc =self .document 
        if doc :
            for attr in doc .attributes :
                if isinstance (attr ,kind ):
                    if not condition or condition (attr ):
                        return doc 
                    return None 

