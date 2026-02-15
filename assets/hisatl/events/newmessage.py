import re 

from .common import EventBuilder ,EventCommon ,name_inner_event ,_into_id_set 
from ..import utils 
from ..tl import types 

@name_inner_event 
class NewMessage (EventBuilder ):
    """"""
    def __init__ (self ,chats =None ,*,blacklist_chats =False ,func =None ,
    incoming =None ,outgoing =None ,
    from_users =None ,forwards =None ,pattern =None ):
        if incoming and outgoing :
            incoming =outgoing =None 
        elif incoming is not None and outgoing is None :
            outgoing =not incoming 
        elif outgoing is not None and incoming is None :
            incoming =not outgoing 
        elif all (x is not None and not x for x in (incoming ,outgoing )):
            raise ValueError ("Don't create an event handler if you "
            "don't want neither incoming nor outgoing!")

        super ().__init__ (chats ,blacklist_chats =blacklist_chats ,func =func )
        self .incoming =incoming 
        self .outgoing =outgoing 
        self .from_users =from_users 
        self .forwards =forwards 
        if isinstance (pattern ,str ):
            self .pattern =re .compile (pattern ).match 
        elif not pattern or callable (pattern ):
            self .pattern =pattern 
        elif hasattr (pattern ,'match')and callable (pattern .match ):
            self .pattern =pattern .match 
        else :
            raise TypeError ('Invalid pattern type given')

        self ._no_check =all (x is None for x in (
        self .chats ,self .incoming ,self .outgoing ,self .pattern ,
        self .from_users ,self .forwards ,self .from_users ,self .func 
        ))

    async def _resolve (self ,client ):
        await super ()._resolve (client )
        self .from_users =await _into_id_set (client ,self .from_users )

    @classmethod 
    def build (cls ,update ,others =None ,self_id =None ):
        if isinstance (update ,
        (types .UpdateNewMessage ,types .UpdateNewChannelMessage )):
            if not isinstance (update .message ,types .Message ):
                return 
            event =cls .Event (update .message )
        elif isinstance (update ,types .UpdateShortMessage ):
            event =cls .Event (types .Message (
            out =update .out ,
            mentioned =update .mentioned ,
            media_unread =update .media_unread ,
            silent =update .silent ,
            id =update .id ,
            peer_id =types .PeerUser (update .user_id ),
            from_id =types .PeerUser (self_id if update .out else update .user_id ),
            message =update .message ,
            date =update .date ,
            fwd_from =update .fwd_from ,
            via_bot_id =update .via_bot_id ,
            reply_to =update .reply_to ,
            entities =update .entities ,
            ttl_period =update .ttl_period 
            ))
        elif isinstance (update ,types .UpdateShortChatMessage ):
            event =cls .Event (types .Message (
            out =update .out ,
            mentioned =update .mentioned ,
            media_unread =update .media_unread ,
            silent =update .silent ,
            id =update .id ,
            from_id =types .PeerUser (self_id if update .out else update .from_id ),
            peer_id =types .PeerChat (update .chat_id ),
            message =update .message ,
            date =update .date ,
            fwd_from =update .fwd_from ,
            via_bot_id =update .via_bot_id ,
            reply_to =update .reply_to ,
            entities =update .entities ,
            ttl_period =update .ttl_period 
            ))
        else :
            return 

        return event 

    def filter (self ,event ):
        if self ._no_check :
            return event 

        if self .incoming and event .message .out :
            return 
        if self .outgoing and not event .message .out :
            return 
        if self .forwards is not None :
            if bool (self .forwards )!=bool (event .message .fwd_from ):
                return 

        if self .from_users is not None :
            if event .message .sender_id not in self .from_users :
                return 

        if self .pattern :
            match =self .pattern (event .message .message or '')
            if not match :
                return 
            event .pattern_match =match 

        return super ().filter (event )

    class Event (EventCommon ):
        """"""
        def __init__ (self ,message ):
            self .__dict__ ['_init']=False 
            super ().__init__ (chat_peer =message .peer_id ,
            msg_id =message .id ,broadcast =bool (message .post ))

            self .pattern_match =None 
            self .message =message 

        def _set_client (self ,client ):
            super ()._set_client (client )
            m =self .message 
            m ._finish_init (client ,self ._entities ,None )
            self .__dict__ ['_init']=True 

        def __getattr__ (self ,item ):
            if item in self .__dict__ :
                return self .__dict__ [item ]
            else :
                return getattr (self .message ,item )

        def __setattr__ (self ,name ,value ):
            if not self .__dict__ ['_init']or name in self .__dict__ :
                self .__dict__ [name ]=value 
            else :
                setattr (self .message ,name ,value )
