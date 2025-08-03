import itertools 
import re 
import typing 

from ..import helpers ,utils 
from ..tl import types 

if typing .TYPE_CHECKING :
    from .telegramclient import TelegramClient 

class MessageParseMethods :

    @property 
    def parse_mode (self :'TelegramClient'):
        """"""
        return self ._parse_mode 

    @parse_mode .setter 
    def parse_mode (self :'TelegramClient',mode :str ):
        self ._parse_mode =utils .sanitize_parse_mode (mode )

    async def _replace_with_mention (self :'TelegramClient',entities ,i ,user ):
        """"""
        try :
            entities [i ]=types .InputMessageEntityMentionName (
            entities [i ].offset ,entities [i ].length ,
            await self .get_input_entity (user )
            )
            return True 
        except (ValueError ,TypeError ):
            return False 

    async def _parse_message_text (self :'TelegramClient',message ,parse_mode ):
        """"""
        if parse_mode ==():
            parse_mode =self ._parse_mode 
        else :
            parse_mode =utils .sanitize_parse_mode (parse_mode )

        if not parse_mode :
            return message ,[]

        original_message =message 
        message ,msg_entities =parse_mode .parse (message )
        if original_message and not message and not msg_entities :
            raise ValueError ("Failed to parse message")

        for i in reversed (range (len (msg_entities ))):
            e =msg_entities [i ]
            if not e .length :

                del msg_entities [i ]
            elif isinstance (e ,types .MessageEntityTextUrl ):
                m =re .match (r'^@|\+|tg://user\?id=(\d+)',e .url )
                if m :
                    user =int (m .group (1 ))if m .group (1 )else e .url 
                    is_mention =await self ._replace_with_mention (msg_entities ,i ,user )
                    if not is_mention :
                        del msg_entities [i ]
            elif isinstance (e ,(types .MessageEntityMentionName ,
            types .InputMessageEntityMentionName )):
                is_mention =await self ._replace_with_mention (msg_entities ,i ,e .user_id )
                if not is_mention :
                    del msg_entities [i ]

        return message ,msg_entities 

    def _get_response_message (self :'TelegramClient',request ,result ,input_chat ):
        """"""
        if isinstance (result ,types .UpdateShort ):
            updates =[result .update ]
            entities ={}
        elif isinstance (result ,(types .Updates ,types .UpdatesCombined )):
            updates =result .updates 
            entities ={utils .get_peer_id (x ):x 
            for x in 
            itertools .chain (result .users ,result .chats )}
        else :
            return None 

        random_to_id ={}
        id_to_message ={}
        for update in updates :
            if isinstance (update ,types .UpdateMessageID ):
                random_to_id [update .random_id ]=update .id 

            elif isinstance (update ,(
            types .UpdateNewChannelMessage ,types .UpdateNewMessage )):
                update .message ._finish_init (self ,entities ,input_chat )

                if hasattr (request ,'random_id')or utils .is_list_like (request ):
                    id_to_message [update .message .id ]=update .message 
                else :
                    return update .message 

            elif isinstance (update ,types .UpdateStory ):
                return update .story 

            elif (isinstance (update ,types .UpdateEditMessage )
            and helpers ._entity_type (request .peer )!=helpers ._EntityType .CHANNEL ):
                update .message ._finish_init (self ,entities ,input_chat )

                if hasattr (request ,'random_id'):
                    id_to_message [update .message .id ]=update .message 
                elif request .id ==update .message .id :
                    return update .message 

            elif (isinstance (update ,types .UpdateEditChannelMessage )
            and utils .get_peer_id (request .peer )==
            utils .get_peer_id (update .message .peer_id )):
                if request .id ==update .message .id :
                    update .message ._finish_init (self ,entities ,input_chat )
                    return update .message 

            elif isinstance (update ,types .UpdateNewScheduledMessage ):
                update .message ._finish_init (self ,entities ,input_chat )

                id_to_message [update .message .id ]=update .message 

            elif isinstance (update ,types .UpdateMessagePoll ):
                if request .media .poll .id ==update .poll_id :
                    m =types .Message (
                    id =request .id ,
                    peer_id =utils .get_peer (request .peer ),
                    media =types .MessageMediaPoll (
                    poll =update .poll ,
                    results =update .results 
                    )
                    )
                    m ._finish_init (self ,entities ,input_chat )
                    return m 

        if request is None :
            return id_to_message 

        random_id =request if isinstance (request ,(int ,list ))else getattr (request ,'random_id',None )
        if random_id is None :

            self ._log [__name__ ].warning (
            'No random_id in %s to map to, returning None message for %s',request ,result )
            return None 

        if not utils .is_list_like (random_id ):
            msg =id_to_message .get (random_to_id .get (random_id ))

            if not msg :
                self ._log [__name__ ].warning (
                'Request %s had missing message mapping %s',request ,result )

            return msg 

        try :
            return [id_to_message [random_to_id [rnd ]]for rnd in random_id ]
        except KeyError :

            self ._log [__name__ ].warning (
            'Request %s had missing message mappings %s',request ,result )

        return [
        id_to_message .get (random_to_id [rnd ])
        if rnd in random_to_id 
        else None 
        for rnd in random_id 
        ]

