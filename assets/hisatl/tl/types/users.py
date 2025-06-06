""""""
from ...tl .tlobject import TLObject 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeChat ,TypeUser ,TypeUserFull 

class UserFull (TLObject ):
    CONSTRUCTOR_ID =0x3b6d152e 
    SUBCLASS_OF_ID =0x83df9df5 

    def __init__ (self ,full_user :'TypeUserFull',chats :List ['TypeChat'],users :List ['TypeUser']):
        """"""
        self .full_user =full_user 
        self .chats =chats 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'UserFull',
        'full_user':self .full_user .to_dict ()if isinstance (self .full_user ,TLObject )else self .full_user ,
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'.\x15m;',
        self .full_user ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _full_user =reader .tgread_object ()
        reader .read_int ()
        _chats =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _chats .append (_x )

        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        return cls (full_user =_full_user ,chats =_chats ,users =_users )

