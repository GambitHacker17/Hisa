from .common import name_inner_event 
from .newmessage import NewMessage 
from ..tl import types 

@name_inner_event 
class MessageEdited (NewMessage ):
    """"""
    @classmethod 
    def build (cls ,update ,others =None ,self_id =None ):
        if isinstance (update ,(types .UpdateEditMessage ,
        types .UpdateEditChannelMessage )):
            return cls .Event (update .message )

    class Event (NewMessage .Event ):
        pass 
