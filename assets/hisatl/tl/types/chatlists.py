""""""
from ...tl .tlobject import TLObject 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeChat ,TypeDialogFilter ,TypeExportedChatlistInvite ,TypePeer ,TypeUser 

class ChatlistInvite (TLObject ):
    CONSTRUCTOR_ID =0x1dcd839d 
    SUBCLASS_OF_ID =0x41720e75 

    def __init__ (self ,title :str ,peers :List ['TypePeer'],chats :List ['TypeChat'],users :List ['TypeUser'],emoticon :Optional [str ]=None ):
        """"""
        self .title =title 
        self .peers =peers 
        self .chats =chats 
        self .users =users 
        self .emoticon =emoticon 

    def to_dict (self ):
        return {
        '_':'ChatlistInvite',
        'title':self .title ,
        'peers':[]if self .peers is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .peers ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ],
        'emoticon':self .emoticon 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x9d\x83\xcd\x1d',
        struct .pack ('<I',(0 if self .emoticon is None or self .emoticon is False else 1 )),
        self .serialize_bytes (self .title ),
        b''if self .emoticon is None or self .emoticon is False else (self .serialize_bytes (self .emoticon )),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .peers )),b''.join (x ._bytes ()for x in self .peers ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _title =reader .tgread_string ()
        if flags &1 :
            _emoticon =reader .tgread_string ()
        else :
            _emoticon =None 
        reader .read_int ()
        _peers =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _peers .append (_x )

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

        return cls (title =_title ,peers =_peers ,chats =_chats ,users =_users ,emoticon =_emoticon )

class ChatlistInviteAlready (TLObject ):
    CONSTRUCTOR_ID =0xfa87f659 
    SUBCLASS_OF_ID =0x41720e75 

    def __init__ (self ,filter_id :int ,missing_peers :List ['TypePeer'],already_peers :List ['TypePeer'],chats :List ['TypeChat'],users :List ['TypeUser']):
        """"""
        self .filter_id =filter_id 
        self .missing_peers =missing_peers 
        self .already_peers =already_peers 
        self .chats =chats 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'ChatlistInviteAlready',
        'filter_id':self .filter_id ,
        'missing_peers':[]if self .missing_peers is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .missing_peers ],
        'already_peers':[]if self .already_peers is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .already_peers ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'Y\xf6\x87\xfa',
        struct .pack ('<i',self .filter_id ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .missing_peers )),b''.join (x ._bytes ()for x in self .missing_peers ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .already_peers )),b''.join (x ._bytes ()for x in self .already_peers ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _filter_id =reader .read_int ()
        reader .read_int ()
        _missing_peers =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _missing_peers .append (_x )

        reader .read_int ()
        _already_peers =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _already_peers .append (_x )

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

        return cls (filter_id =_filter_id ,missing_peers =_missing_peers ,already_peers =_already_peers ,chats =_chats ,users =_users )

class ChatlistUpdates (TLObject ):
    CONSTRUCTOR_ID =0x93bd878d 
    SUBCLASS_OF_ID =0x7d1641ea 

    def __init__ (self ,missing_peers :List ['TypePeer'],chats :List ['TypeChat'],users :List ['TypeUser']):
        """"""
        self .missing_peers =missing_peers 
        self .chats =chats 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'ChatlistUpdates',
        'missing_peers':[]if self .missing_peers is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .missing_peers ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x8d\x87\xbd\x93',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .missing_peers )),b''.join (x ._bytes ()for x in self .missing_peers ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _missing_peers =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _missing_peers .append (_x )

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

        return cls (missing_peers =_missing_peers ,chats =_chats ,users =_users )

class ExportedChatlistInvite (TLObject ):
    CONSTRUCTOR_ID =0x10e6e3a6 
    SUBCLASS_OF_ID =0xc2694ee9 

    def __init__ (self ,filter :'TypeDialogFilter',invite :'TypeExportedChatlistInvite'):
        """"""
        self .filter =filter 
        self .invite =invite 

    def to_dict (self ):
        return {
        '_':'ExportedChatlistInvite',
        'filter':self .filter .to_dict ()if isinstance (self .filter ,TLObject )else self .filter ,
        'invite':self .invite .to_dict ()if isinstance (self .invite ,TLObject )else self .invite 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xa6\xe3\xe6\x10',
        self .filter ._bytes (),
        self .invite ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _filter =reader .tgread_object ()
        _invite =reader .tgread_object ()
        return cls (filter =_filter ,invite =_invite )

class ExportedInvites (TLObject ):
    CONSTRUCTOR_ID =0x10ab6dc7 
    SUBCLASS_OF_ID =0xe6c209c0 

    def __init__ (self ,invites :List ['TypeExportedChatlistInvite'],chats :List ['TypeChat'],users :List ['TypeUser']):
        """"""
        self .invites =invites 
        self .chats =chats 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'ExportedInvites',
        'invites':[]if self .invites is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .invites ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc7m\xab\x10',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .invites )),b''.join (x ._bytes ()for x in self .invites ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _invites =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _invites .append (_x )

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

        return cls (invites =_invites ,chats =_chats ,users =_users )

