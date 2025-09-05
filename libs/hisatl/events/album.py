import asyncio 
import time 
import weakref 

from .common import EventBuilder ,EventCommon ,name_inner_event 
from ..import utils 
from ..tl import types 
from ..tl .custom .sendergetter import SenderGetter 

_IGNORE_MAX_SIZE =100 
_IGNORE_MAX_AGE =5 

_IGNORE_DICT ={}

_HACK_DELAY =0.5 

class AlbumHack :
    """"""
    def __init__ (self ,client ,event ):

        self ._client =weakref .ref (client )
        self ._event =event 
        self ._due =client .loop .time ()+_HACK_DELAY 

        client .loop .create_task (self .deliver_event ())

    def extend (self ,messages ):
        client =self ._client ()
        if client :
            self ._event .messages .extend (messages )
            self ._due =client .loop .time ()+_HACK_DELAY 

    async def deliver_event (self ):
        while True :
            client =self ._client ()
            if client is None :
                return 

            diff =self ._due -client .loop .time ()
            if diff <=0 :

                await client ._dispatch_event (self ._event )
                return 

            del client 
            await asyncio .sleep (diff )

@name_inner_event 
class Album (EventBuilder ):
    """"""

    def __init__ (
    self ,chats =None ,*,blacklist_chats =False ,func =None ):
        super ().__init__ (chats ,blacklist_chats =blacklist_chats ,func =func )

    @classmethod 
    def build (cls ,update ,others =None ,self_id =None ):

        others =[update ]

        if isinstance (update ,
        (types .UpdateNewMessage ,types .UpdateNewChannelMessage )):
            if not isinstance (update .message ,types .Message ):
                return 

            group =update .message .grouped_id 
            if group is None :
                return 

            if _IGNORE_DICT .pop (id (update ),None ):
                return 

            now =time .time ()
            if len (_IGNORE_DICT )>_IGNORE_MAX_SIZE :
                for i in [i for i ,t in _IGNORE_DICT .items ()if now -t >_IGNORE_MAX_AGE ]:
                    del _IGNORE_DICT [i ]

            for u in others :
                if u is not update :
                    _IGNORE_DICT [id (u )]=now 

            return cls .Event ([
            u .message for u in others 
            if (isinstance (u ,(types .UpdateNewMessage ,types .UpdateNewChannelMessage ))
            and isinstance (u .message ,types .Message )
            and u .message .grouped_id ==group )
            ])

    def filter (self ,event ):

        if len (event .messages )>1 :
            return super ().filter (event )

    class Event (EventCommon ,SenderGetter ):
        """"""
        def __init__ (self ,messages ):
            message =messages [0 ]
            super ().__init__ (chat_peer =message .peer_id ,
            msg_id =message .id ,broadcast =bool (message .post ))
            SenderGetter .__init__ (self ,message .sender_id )
            self .messages =messages 

        def _set_client (self ,client ):
            super ()._set_client (client )
            self ._sender ,self ._input_sender =utils ._get_entity_pair (
            self .sender_id ,self ._entities ,client ._entity_cache )

            for msg in self .messages :
                msg ._finish_init (client ,self ._entities ,None )

            if len (self .messages )==1 :

                hack =client ._albums .get (self .grouped_id )
                if hack is None :
                    client ._albums [self .grouped_id ]=AlbumHack (client ,self )
                else :
                    hack .extend (self .messages )

        @property 
        def grouped_id (self ):
            """"""
            return self .messages [0 ].grouped_id 

        @property 
        def text (self ):
            """"""
            return next ((m .text for m in self .messages if m .text ),'')

        @property 
        def raw_text (self ):
            """"""
            return next ((m .raw_text for m in self .messages if m .raw_text ),'')

        @property 
        def is_reply (self ):
            """"""

            return self .messages [0 ].is_reply 

        @property 
        def forward (self ):
            """"""

            return self .messages [0 ].forward 

        async def get_reply_message (self ):
            """"""
            return await self .messages [0 ].get_reply_message ()

        async def respond (self ,*args ,**kwargs ):
            """"""
            return await self .messages [0 ].respond (*args ,**kwargs )

        async def reply (self ,*args ,**kwargs ):
            """"""
            return await self .messages [0 ].reply (*args ,**kwargs )

        async def forward_to (self ,*args ,**kwargs ):
            """"""
            if self ._client :
                kwargs ['messages']=self .messages 
                kwargs ['from_peer']=await self .get_input_chat ()
                return await self ._client .forward_messages (*args ,**kwargs )

        async def edit (self ,*args ,**kwargs ):
            """"""
            for msg in self .messages :
                if msg .raw_text :
                    return await msg .edit (*args ,**kwargs )

            return await self .messages [0 ].edit (*args ,**kwargs )

        async def delete (self ,*args ,**kwargs ):
            """"""
            if self ._client :
                return await self ._client .delete_messages (
                await self .get_input_chat (),self .messages ,
                *args ,**kwargs 
                )

        async def mark_read (self ):
            """"""
            if self ._client :
                await self ._client .send_read_acknowledge (
                await self .get_input_chat (),max_id =self .messages [-1 ].id )

        async def pin (self ,*,notify =False ):
            """"""
            return await self .messages [0 ].pin (notify =notify )

        def __len__ (self ):
            """"""
            return len (self .messages )

        def __iter__ (self ):
            """"""
            return iter (self .messages )

        def __getitem__ (self ,n ):
            """"""
            return self .messages [n ]
