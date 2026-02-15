from .raw import Raw 
from .album import Album 
from .chataction import ChatAction 
from .messagedeleted import MessageDeleted 
from .messageedited import MessageEdited 
from .messageread import MessageRead 
from .newmessage import NewMessage 
from .userupdate import UserUpdate 
from .callbackquery import CallbackQuery 
from .inlinequery import InlineQuery 

_HANDLERS_ATTRIBUTE ='__tl.handlers'

class StopPropagation (Exception ):
    """"""

    pass 

def register (event =None ):
    """"""
    if isinstance (event ,type ):
        event =event ()
    elif not event :
        event =Raw ()

    def decorator (callback ):
        handlers =getattr (callback ,_HANDLERS_ATTRIBUTE ,[])
        handlers .append (event )
        setattr (callback ,_HANDLERS_ATTRIBUTE ,handlers )
        return callback 

    return decorator 

def unregister (callback ,event =None ):
    """"""
    found =0 
    if event and not isinstance (event ,type ):
        event =type (event )

    handlers =getattr (callback ,_HANDLERS_ATTRIBUTE ,[])
    handlers .append ((event ,callback ))
    i =len (handlers )
    while i :
        i -=1 
        ev =handlers [i ]
        if not event or isinstance (ev ,event ):
            del handlers [i ]
            found +=1 

    return found 

def is_handler (callback ):
    """"""
    return hasattr (callback ,_HANDLERS_ATTRIBUTE )

def list (callback ):
    """"""
    return getattr (callback ,_HANDLERS_ATTRIBUTE ,[])[:]

def _get_handlers (callback ):
    """"""
    return getattr (callback ,_HANDLERS_ATTRIBUTE ,None )
