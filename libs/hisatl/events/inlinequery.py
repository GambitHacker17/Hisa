import inspect 
import re 

import asyncio 

from .common import EventBuilder ,EventCommon ,name_inner_event 
from ..import utils ,helpers 
from ..tl import types ,functions ,custom 
from ..tl .custom .sendergetter import SenderGetter 

@name_inner_event 
class InlineQuery (EventBuilder ):
    """"""
    def __init__ (
    self ,users =None ,*,blacklist_users =False ,func =None ,pattern =None ):
        super ().__init__ (users ,blacklist_chats =blacklist_users ,func =func )

        if isinstance (pattern ,str ):
            self .pattern =re .compile (pattern ).match 
        elif not pattern or callable (pattern ):
            self .pattern =pattern 
        elif hasattr (pattern ,'match')and callable (pattern .match ):
            self .pattern =pattern .match 
        else :
            raise TypeError ('Invalid pattern type given')

    @classmethod 
    def build (cls ,update ,others =None ,self_id =None ):
        if isinstance (update ,types .UpdateBotInlineQuery ):
            return cls .Event (update )

    def filter (self ,event ):
        if self .pattern :
            match =self .pattern (event .text )
            if not match :
                return 
            event .pattern_match =match 

        return super ().filter (event )

    class Event (EventCommon ,SenderGetter ):
        """"""
        def __init__ (self ,query ):
            super ().__init__ (chat_peer =types .PeerUser (query .user_id ))
            SenderGetter .__init__ (self ,query .user_id )
            self .query =query 
            self .pattern_match =None 
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
        def text (self ):
            """"""
            return self .query .query 

        @property 
        def offset (self ):
            """"""
            return self .query .offset 

        @property 
        def geo (self ):
            """"""
            return self .query .geo 

        @property 
        def builder (self ):
            """"""
            return custom .InlineBuilder (self ._client )

        async def answer (
        self ,results =None ,cache_time =0 ,*,
        gallery =False ,next_offset =None ,private =False ,
        switch_pm =None ,switch_pm_param =''):
            """"""
            if self ._answered :
                return 

            if results :
                futures =[self ._as_future (x )for x in results ]

                await asyncio .wait (futures )

                results =[x .result ()for x in futures ]
            else :
                results =[]

            if switch_pm :
                switch_pm =types .InlineBotSwitchPM (switch_pm ,switch_pm_param )

            return await self ._client (
            functions .messages .SetInlineBotResultsRequest (
            query_id =self .query .query_id ,
            results =results ,
            cache_time =cache_time ,
            gallery =gallery ,
            next_offset =next_offset ,
            private =private ,
            switch_pm =switch_pm 
            )
            )

        @staticmethod 
        def _as_future (obj ):
            if inspect .isawaitable (obj ):
                return asyncio .ensure_future (obj )

            f =helpers .get_running_loop ().create_future ()
            f .set_result (obj )
            return f 
