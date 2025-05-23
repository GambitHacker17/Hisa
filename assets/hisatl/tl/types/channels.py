""""""
from ...tl .tlobject import TLObject 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeChannelAdminLogEvent ,TypeChannelParticipant ,TypeChat ,TypeSendAsPeer ,TypeUser 

class AdminLogResults (TLObject ):
    CONSTRUCTOR_ID =0xed8af74d 
    SUBCLASS_OF_ID =0x51f076bc 

    def __init__ (self ,events :List ['TypeChannelAdminLogEvent'],chats :List ['TypeChat'],users :List ['TypeUser']):
        """"""
        self .events =events 
        self .chats =chats 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'AdminLogResults',
        'events':[]if self .events is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .events ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'M\xf7\x8a\xed',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .events )),b''.join (x ._bytes ()for x in self .events ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _events =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _events .append (_x )

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

        return cls (events =_events ,chats =_chats ,users =_users )

class ChannelParticipant (TLObject ):
    CONSTRUCTOR_ID =0xdfb80317 
    SUBCLASS_OF_ID =0x6658151a 

    def __init__ (self ,participant :'TypeChannelParticipant',chats :List ['TypeChat'],users :List ['TypeUser']):
        """"""
        self .participant =participant 
        self .chats =chats 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'ChannelParticipant',
        'participant':self .participant .to_dict ()if isinstance (self .participant ,TLObject )else self .participant ,
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x17\x03\xb8\xdf',
        self .participant ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _participant =reader .tgread_object ()
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

        return cls (participant =_participant ,chats =_chats ,users =_users )

class ChannelParticipants (TLObject ):
    CONSTRUCTOR_ID =0x9ab0feaf 
    SUBCLASS_OF_ID =0xe60a6e64 

    def __init__ (self ,count :int ,participants :List ['TypeChannelParticipant'],chats :List ['TypeChat'],users :List ['TypeUser']):
        """"""
        self .count =count 
        self .participants =participants 
        self .chats =chats 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'ChannelParticipants',
        'count':self .count ,
        'participants':[]if self .participants is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .participants ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xaf\xfe\xb0\x9a',
        struct .pack ('<i',self .count ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .participants )),b''.join (x ._bytes ()for x in self .participants ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _count =reader .read_int ()
        reader .read_int ()
        _participants =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _participants .append (_x )

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

        return cls (count =_count ,participants =_participants ,chats =_chats ,users =_users )

class ChannelParticipantsNotModified (TLObject ):
    CONSTRUCTOR_ID =0xf0173fe9 
    SUBCLASS_OF_ID =0xe60a6e64 

    def to_dict (self ):
        return {
        '_':'ChannelParticipantsNotModified'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xe9?\x17\xf0',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class SendAsPeers (TLObject ):
    CONSTRUCTOR_ID =0xf496b0c6 
    SUBCLASS_OF_ID =0x38cb8d21 

    def __init__ (self ,peers :List ['TypeSendAsPeer'],chats :List ['TypeChat'],users :List ['TypeUser']):
        """"""
        self .peers =peers 
        self .chats =chats 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'SendAsPeers',
        'peers':[]if self .peers is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .peers ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc6\xb0\x96\xf4',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .peers )),b''.join (x ._bytes ()for x in self .peers ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
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

        return cls (peers =_peers ,chats =_chats ,users =_users )

