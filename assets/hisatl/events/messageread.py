from .common import EventBuilder ,EventCommon ,name_inner_event 
from ..import utils 
from ..tl import types 

@name_inner_event 
class MessageRead (EventBuilder ):
    """"""
    def __init__ (
    self ,chats =None ,*,blacklist_chats =False ,func =None ,inbox =False ):
        super ().__init__ (chats ,blacklist_chats =blacklist_chats ,func =func )
        self .inbox =inbox 

    @classmethod 
    def build (cls ,update ,others =None ,self_id =None ):
        if isinstance (update ,types .UpdateReadHistoryInbox ):
            return cls .Event (update .peer ,update .max_id ,False )
        elif isinstance (update ,types .UpdateReadHistoryOutbox ):
            return cls .Event (update .peer ,update .max_id ,True )
        elif isinstance (update ,types .UpdateReadChannelInbox ):
            return cls .Event (types .PeerChannel (update .channel_id ),
            update .max_id ,False )
        elif isinstance (update ,types .UpdateReadChannelOutbox ):
            return cls .Event (types .PeerChannel (update .channel_id ),
            update .max_id ,True )
        elif isinstance (update ,types .UpdateReadMessagesContents ):
            return cls .Event (message_ids =update .messages ,
            contents =True )
        elif isinstance (update ,types .UpdateChannelReadMessagesContents ):
            return cls .Event (types .PeerChannel (update .channel_id ),
            message_ids =update .messages ,
            contents =True )

    def filter (self ,event ):
        if self .inbox ==event .outbox :
            return 

        return super ().filter (event )

    class Event (EventCommon ):
        """"""
        def __init__ (self ,peer =None ,max_id =None ,out =False ,contents =False ,
        message_ids =None ):
            self .outbox =out 
            self .contents =contents 
            self ._message_ids =message_ids or []
            self ._messages =None 
            self .max_id =max_id or max (message_ids or [],default =None )
            super ().__init__ (peer ,self .max_id )

        @property 
        def inbox (self ):
            """"""
            return not self .outbox 

        @property 
        def message_ids (self ):
            """"""
            return self ._message_ids 

        async def get_messages (self ):
            """"""
            if self ._messages is None :
                chat =await self .get_input_chat ()
                if not chat :
                    self ._messages =[]
                else :
                    self ._messages =await self ._client .get_messages (
                    chat ,ids =self ._message_ids )

            return self ._messages 

        def is_read (self ,message ):
            """"""
            if utils .is_list_like (message ):
                return [(m if isinstance (m ,int )else m .id )<=self .max_id 
                for m in message ]
            else :
                return (message if isinstance (message ,int )
                else message .id )<=self .max_id 

        def __contains__ (self ,message ):
            """"""
            if utils .is_list_like (message ):
                return all (self .is_read (message ))
            else :
                return self .is_read (message )
