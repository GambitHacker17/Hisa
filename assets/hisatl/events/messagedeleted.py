from .common import EventBuilder ,EventCommon ,name_inner_event 
from ..tl import types 

@name_inner_event 
class MessageDeleted (EventBuilder ):
    """"""
    @classmethod 
    def build (cls ,update ,others =None ,self_id =None ):
        if isinstance (update ,types .UpdateDeleteMessages ):
            return cls .Event (
            deleted_ids =update .messages ,
            peer =None 
            )
        elif isinstance (update ,types .UpdateDeleteChannelMessages ):
            return cls .Event (
            deleted_ids =update .messages ,
            peer =types .PeerChannel (update .channel_id )
            )

    class Event (EventCommon ):
        def __init__ (self ,deleted_ids ,peer ):
            super ().__init__ (
            chat_peer =peer ,msg_id =(deleted_ids or [0 ])[0 ]
            )
            self .deleted_id =None if not deleted_ids else deleted_ids [0 ]
            self .deleted_ids =deleted_ids 
