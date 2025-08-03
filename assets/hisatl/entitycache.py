import inspect 
import itertools 

from .import utils 
from .tl import types 

_has_field ={
('user_id',int ):[],
('chat_id',int ):[],
('channel_id',int ):[],
('peer','TypePeer'):[],
('peer','TypeDialogPeer'):[],
('message','TypeMessage'):[],
}

def _fill ():
    for name in dir (types ):
        update =getattr (types ,name )
        if getattr (update ,'SUBCLASS_OF_ID',None )==0x9f89304e :
            cid =update .CONSTRUCTOR_ID 
            sig =inspect .signature (update .__init__ )
            for param in sig .parameters .values ():
                vec =_has_field .get ((param .name ,param .annotation ))
                if vec is not None :
                    vec .append (cid )

    if not all (_has_field .values ()):
        raise RuntimeError ('FIXME: Did the init signature or updates change?')

_fill ()

class EntityCache :
    """"""
    def add (self ,entities ):
        """"""
        if not utils .is_list_like (entities ):

            entities =itertools .chain (
            getattr (entities ,'chats',[]),
            getattr (entities ,'users',[]),
            (hasattr (entities ,'user')and [entities .user ])or []
            )

        for entity in entities :
            try :
                pid =utils .get_peer_id (entity )
                if pid not in self .__dict__ :

                    self .__dict__ [pid ]=utils .get_input_peer (entity )
            except TypeError :
                pass 

    def __getitem__ (self ,item ):
        """"""
        if not isinstance (item ,int )or item <0 :
            try :
                return self .__dict__ [utils .get_peer_id (item )]
            except TypeError :
                raise KeyError ('Invalid key will not have entity')from None 

        for cls in (types .PeerUser ,types .PeerChat ,types .PeerChannel ):
            result =self .__dict__ .get (utils .get_peer_id (cls (item )))
            if result :
                return result 

        raise KeyError ('No cached entity for the given key')

    def clear (self ):
        """"""
        self .__dict__ .clear ()

    def ensure_cached (
    self ,
    update ,
    has_user_id =frozenset (_has_field [('user_id',int )]),
    has_chat_id =frozenset (_has_field [('chat_id',int )]),
    has_channel_id =frozenset (_has_field [('channel_id',int )]),
    has_peer =frozenset (_has_field [('peer','TypePeer')]+_has_field [('peer','TypeDialogPeer')]),
    has_message =frozenset (_has_field [('message','TypeMessage')])
    ):
        """"""

        dct =self .__dict__ 
        cid =update .CONSTRUCTOR_ID 
        if cid in has_user_id and update .user_id not in dct :
            return False 

        if cid in has_chat_id and utils .get_peer_id (types .PeerChat (update .chat_id ))not in dct :
            return False 

        if cid in has_channel_id and utils .get_peer_id (types .PeerChannel (update .channel_id ))not in dct :
            return False 

        if cid in has_peer and utils .get_peer_id (update .peer )not in dct :
            return False 

        if cid in has_message :
            x =update .message 
            y =getattr (x ,'peer_id',None )
            if y and utils .get_peer_id (y )not in dct :
                return False 

            y =getattr (x ,'from_id',None )
            if y and utils .get_peer_id (y )not in dct :
                return False 

        return True 
