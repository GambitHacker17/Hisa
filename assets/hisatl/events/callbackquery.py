import re 
import struct 

from .common import EventBuilder ,EventCommon ,name_inner_event 
from ..import utils 
from ..tl import types ,functions 
from ..tl .custom .sendergetter import SenderGetter 

@name_inner_event 
class CallbackQuery (EventBuilder ):
    """"""
    def __init__ (
    self ,chats =None ,*,blacklist_chats =False ,func =None ,data =None ,pattern =None ):
        super ().__init__ (chats ,blacklist_chats =blacklist_chats ,func =func )

        if data and pattern :
            raise ValueError ("Only pass either data or pattern not both.")

        if isinstance (data ,str ):
            data =data .encode ('utf-8')
        if isinstance (pattern ,str ):
            pattern =pattern .encode ('utf-8')

        match =data if data else pattern 

        if isinstance (match ,bytes ):
            self .match =data if data else re .compile (pattern ).match 
        elif not match or callable (match ):
            self .match =match 
        elif hasattr (match ,'match')and callable (match .match ):
            if not isinstance (getattr (match ,'pattern',b''),bytes ):
                match =re .compile (match .pattern .encode ('utf-8'),
                match .flags &(~re .UNICODE ))

            self .match =match .match 
        else :
            raise TypeError ('Invalid data or pattern type given')

        self ._no_check =all (x is None for x in (
        self .chats ,self .func ,self .match ,
        ))

    @classmethod 
    def build (cls ,update ,others =None ,self_id =None ):
        if isinstance (update ,types .UpdateBotCallbackQuery ):
            return cls .Event (update ,update .peer ,update .msg_id )
        elif isinstance (update ,types .UpdateInlineBotCallbackQuery ):

            mid ,pid =struct .unpack ('<ii',struct .pack ('<q',update .msg_id .id ))
            peer =types .PeerChannel (-pid )if pid <0 else types .PeerUser (pid )
            return cls .Event (update ,peer ,mid )

    def filter (self ,event ):

        if self ._no_check :
            return event 

        if self .chats is not None :
            inside =event .query .chat_instance in self .chats 
            if event .chat_id :
                inside |=event .chat_id in self .chats 

            if inside ==self .blacklist_chats :
                return 

        if self .match :
            if callable (self .match ):
                event .data_match =event .pattern_match =self .match (event .query .data )
                if not event .data_match :
                    return 
            elif event .query .data !=self .match :
                return 

        if self .func :

            return self .func (event )
        return True 

    class Event (EventCommon ,SenderGetter ):
        """"""
        def __init__ (self ,query ,peer ,msg_id ):
            super ().__init__ (peer ,msg_id =msg_id )
            SenderGetter .__init__ (self ,query .user_id )
            self .query =query 
            self .data_match =None 
            self .pattern_match =None 
            self ._message =None 
            self ._answered =False 

        def _set_client (self ,client ):
            super ()._set_client (client )
            self ._sender ,self ._input_sender =utils ._get_entity_pair (
            self .sender_id ,self ._entities ,client ._entity_cache )

        @property 
        def id (self ):
            """"""
            return self .query .query_id 

        @property 
        def message_id (self ):
            """"""
            return self ._message_id 

        @property 
        def data (self ):
            """"""
            return self .query .data 

        @property 
        def chat_instance (self ):
            """"""
            return self .query .chat_instance 

        async def get_message (self ):
            """"""
            if self ._message is not None :
                return self ._message 

            try :
                chat =await self .get_input_chat ()if self .is_channel else None 
                self ._message =await self ._client .get_messages (
                chat ,ids =self ._message_id )
            except ValueError :
                return 

            return self ._message 

        async def _refetch_sender (self ):
            self ._sender =self ._entities .get (self .sender_id )
            if not self ._sender :
                return 

            self ._input_sender =utils .get_input_peer (self ._chat )
            if not getattr (self ._input_sender ,'access_hash',True ):

                try :
                    self ._input_sender =self ._client ._entity_cache [self ._sender_id ]
                except KeyError :
                    m =await self .get_message ()
                    if m :
                        self ._sender =m ._sender 
                        self ._input_sender =m ._input_sender 

        async def answer (
        self ,message =None ,cache_time =0 ,*,url =None ,alert =False ):
            """"""
            if self ._answered :
                return 

            self ._answered =True 
            return await self ._client (
            functions .messages .SetBotCallbackAnswerRequest (
            query_id =self .query .query_id ,
            cache_time =cache_time ,
            alert =alert ,
            message =message ,
            url =url 
            )
            )

        @property 
        def via_inline (self ):
            """"""
            return isinstance (self .query ,types .UpdateInlineBotCallbackQuery )

        async def respond (self ,*args ,**kwargs ):
            """"""
            self ._client .loop .create_task (self .answer ())
            return await self ._client .send_message (
            await self .get_input_chat (),*args ,**kwargs )

        async def reply (self ,*args ,**kwargs ):
            """"""
            self ._client .loop .create_task (self .answer ())
            kwargs ['reply_to']=self .query .msg_id 
            return await self ._client .send_message (
            await self .get_input_chat (),*args ,**kwargs )

        async def edit (self ,*args ,**kwargs ):
            """"""
            self ._client .loop .create_task (self .answer ())
            if isinstance (self .query .msg_id ,types .InputBotInlineMessageID ):
                return await self ._client .edit_message (
                self .query .msg_id ,*args ,**kwargs 
                )
            else :
                return await self ._client .edit_message (
                await self .get_input_chat (),self .query .msg_id ,
                *args ,**kwargs 
                )

        async def delete (self ,*args ,**kwargs ):
            """"""
            self ._client .loop .create_task (self .answer ())
            if isinstance (self .query .msg_id ,(types .InputBotInlineMessageID ,types .InputBotInlineMessageID64 )):
                raise TypeError ('Inline messages cannot be deleted as there is no API request available to do so')
            return await self ._client .delete_messages (
            await self .get_input_chat (),[self .query .msg_id ],
            *args ,**kwargs 
            )
