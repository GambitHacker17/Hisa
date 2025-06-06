""""""
from ...tl .tlobject import TLObject 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeChat ,TypeGroupCall ,TypeGroupCallParticipant ,TypeGroupCallStreamChannel ,TypePeer ,TypePhoneCall ,TypeUser 

class ExportedGroupCallInvite (TLObject ):
    CONSTRUCTOR_ID =0x204bd158 
    SUBCLASS_OF_ID =0x3b3bfe8f 

    def __init__ (self ,link :str ):
        """"""
        self .link =link 

    def to_dict (self ):
        return {
        '_':'ExportedGroupCallInvite',
        'link':self .link 
        }

    def _bytes (self ):
        return b''.join ((
        b'X\xd1K ',
        self .serialize_bytes (self .link ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _link =reader .tgread_string ()
        return cls (link =_link )

class GroupCall (TLObject ):
    CONSTRUCTOR_ID =0x9e727aad 
    SUBCLASS_OF_ID =0x304116be 

    def __init__ (self ,call :'TypeGroupCall',participants :List ['TypeGroupCallParticipant'],participants_next_offset :str ,chats :List ['TypeChat'],users :List ['TypeUser']):
        """"""
        self .call =call 
        self .participants =participants 
        self .participants_next_offset =participants_next_offset 
        self .chats =chats 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'GroupCall',
        'call':self .call .to_dict ()if isinstance (self .call ,TLObject )else self .call ,
        'participants':[]if self .participants is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .participants ],
        'participants_next_offset':self .participants_next_offset ,
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xadzr\x9e',
        self .call ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .participants )),b''.join (x ._bytes ()for x in self .participants ),
        self .serialize_bytes (self .participants_next_offset ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _call =reader .tgread_object ()
        reader .read_int ()
        _participants =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _participants .append (_x )

        _participants_next_offset =reader .tgread_string ()
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

        return cls (call =_call ,participants =_participants ,participants_next_offset =_participants_next_offset ,chats =_chats ,users =_users )

class GroupCallStreamChannels (TLObject ):
    CONSTRUCTOR_ID =0xd0e482b2 
    SUBCLASS_OF_ID =0x9157c5e4 

    def __init__ (self ,channels :List ['TypeGroupCallStreamChannel']):
        """"""
        self .channels =channels 

    def to_dict (self ):
        return {
        '_':'GroupCallStreamChannels',
        'channels':[]if self .channels is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .channels ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xb2\x82\xe4\xd0',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .channels )),b''.join (x ._bytes ()for x in self .channels ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _channels =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _channels .append (_x )

        return cls (channels =_channels )

class GroupCallStreamRtmpUrl (TLObject ):
    CONSTRUCTOR_ID =0x2dbf3432 
    SUBCLASS_OF_ID =0xd1f515cb 

    def __init__ (self ,url :str ,key :str ):
        """"""
        self .url =url 
        self .key =key 

    def to_dict (self ):
        return {
        '_':'GroupCallStreamRtmpUrl',
        'url':self .url ,
        'key':self .key 
        }

    def _bytes (self ):
        return b''.join ((
        b'24\xbf-',
        self .serialize_bytes (self .url ),
        self .serialize_bytes (self .key ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _url =reader .tgread_string ()
        _key =reader .tgread_string ()
        return cls (url =_url ,key =_key )

class GroupParticipants (TLObject ):
    CONSTRUCTOR_ID =0xf47751b6 
    SUBCLASS_OF_ID =0x72d304f4 

    def __init__ (self ,count :int ,participants :List ['TypeGroupCallParticipant'],next_offset :str ,chats :List ['TypeChat'],users :List ['TypeUser'],version :int ):
        """"""
        self .count =count 
        self .participants =participants 
        self .next_offset =next_offset 
        self .chats =chats 
        self .users =users 
        self .version =version 

    def to_dict (self ):
        return {
        '_':'GroupParticipants',
        'count':self .count ,
        'participants':[]if self .participants is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .participants ],
        'next_offset':self .next_offset ,
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ],
        'version':self .version 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xb6Qw\xf4',
        struct .pack ('<i',self .count ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .participants )),b''.join (x ._bytes ()for x in self .participants ),
        self .serialize_bytes (self .next_offset ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        struct .pack ('<i',self .version ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _count =reader .read_int ()
        reader .read_int ()
        _participants =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _participants .append (_x )

        _next_offset =reader .tgread_string ()
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

        _version =reader .read_int ()
        return cls (count =_count ,participants =_participants ,next_offset =_next_offset ,chats =_chats ,users =_users ,version =_version )

class JoinAsPeers (TLObject ):
    CONSTRUCTOR_ID =0xafe5623f 
    SUBCLASS_OF_ID =0xb4b770fb 

    def __init__ (self ,peers :List ['TypePeer'],chats :List ['TypeChat'],users :List ['TypeUser']):
        """"""
        self .peers =peers 
        self .chats =chats 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'JoinAsPeers',
        'peers':[]if self .peers is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .peers ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'?b\xe5\xaf',
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

class PhoneCall (TLObject ):
    CONSTRUCTOR_ID =0xec82e140 
    SUBCLASS_OF_ID =0xd48afe4f 

    def __init__ (self ,phone_call :'TypePhoneCall',users :List ['TypeUser']):
        """"""
        self .phone_call =phone_call 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'PhoneCall',
        'phone_call':self .phone_call .to_dict ()if isinstance (self .phone_call ,TLObject )else self .phone_call ,
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'@\xe1\x82\xec',
        self .phone_call ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _phone_call =reader .tgread_object ()
        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        return cls (phone_call =_phone_call ,users =_users )

