""""""
from ...tl .tlobject import TLObject 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeChat ,TypePeerStories ,TypeStoriesStealthMode ,TypeStoryItem ,TypeStoryView ,TypeStoryViews ,TypeUser 

class AllStories (TLObject ):
    CONSTRUCTOR_ID =0x6efc5e81 
    SUBCLASS_OF_ID =0x7e60d0cd 

    def __init__ (self ,count :int ,state :str ,peer_stories :List ['TypePeerStories'],chats :List ['TypeChat'],users :List ['TypeUser'],stealth_mode :'TypeStoriesStealthMode',has_more :Optional [bool ]=None ):
        """"""
        self .count =count 
        self .state =state 
        self .peer_stories =peer_stories 
        self .chats =chats 
        self .users =users 
        self .stealth_mode =stealth_mode 
        self .has_more =has_more 

    def to_dict (self ):
        return {
        '_':'AllStories',
        'count':self .count ,
        'state':self .state ,
        'peer_stories':[]if self .peer_stories is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .peer_stories ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ],
        'stealth_mode':self .stealth_mode .to_dict ()if isinstance (self .stealth_mode ,TLObject )else self .stealth_mode ,
        'has_more':self .has_more 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x81^\xfcn',
        struct .pack ('<I',(0 if self .has_more is None or self .has_more is False else 1 )),
        struct .pack ('<i',self .count ),
        self .serialize_bytes (self .state ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .peer_stories )),b''.join (x ._bytes ()for x in self .peer_stories ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        self .stealth_mode ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _has_more =bool (flags &1 )
        _count =reader .read_int ()
        _state =reader .tgread_string ()
        reader .read_int ()
        _peer_stories =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _peer_stories .append (_x )

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

        _stealth_mode =reader .tgread_object ()
        return cls (count =_count ,state =_state ,peer_stories =_peer_stories ,chats =_chats ,users =_users ,stealth_mode =_stealth_mode ,has_more =_has_more )

class AllStoriesNotModified (TLObject ):
    CONSTRUCTOR_ID =0x1158fe3e 
    SUBCLASS_OF_ID =0x7e60d0cd 

    def __init__ (self ,state :str ,stealth_mode :'TypeStoriesStealthMode'):
        """"""
        self .state =state 
        self .stealth_mode =stealth_mode 

    def to_dict (self ):
        return {
        '_':'AllStoriesNotModified',
        'state':self .state ,
        'stealth_mode':self .stealth_mode .to_dict ()if isinstance (self .stealth_mode ,TLObject )else self .stealth_mode 
        }

    def _bytes (self ):
        return b''.join ((
        b'>\xfeX\x11',
        b'\0\0\0\0',
        self .serialize_bytes (self .state ),
        self .stealth_mode ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _state =reader .tgread_string ()
        _stealth_mode =reader .tgread_object ()
        return cls (state =_state ,stealth_mode =_stealth_mode )

class PeerStories (TLObject ):
    CONSTRUCTOR_ID =0xcae68768 
    SUBCLASS_OF_ID =0x9d56cfd0 

    def __init__ (self ,stories :'TypePeerStories',chats :List ['TypeChat'],users :List ['TypeUser']):
        """"""
        self .stories =stories 
        self .chats =chats 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'PeerStories',
        'stories':self .stories .to_dict ()if isinstance (self .stories ,TLObject )else self .stories ,
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'h\x87\xe6\xca',
        self .stories ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _stories =reader .tgread_object ()
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

        return cls (stories =_stories ,chats =_chats ,users =_users )

class Stories (TLObject ):
    CONSTRUCTOR_ID =0x5dd8c3c8 
    SUBCLASS_OF_ID =0x251c0c2c 

    def __init__ (self ,count :int ,stories :List ['TypeStoryItem'],chats :List ['TypeChat'],users :List ['TypeUser']):
        """"""
        self .count =count 
        self .stories =stories 
        self .chats =chats 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'Stories',
        'count':self .count ,
        'stories':[]if self .stories is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .stories ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc8\xc3\xd8]',
        struct .pack ('<i',self .count ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .stories )),b''.join (x ._bytes ()for x in self .stories ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _count =reader .read_int ()
        reader .read_int ()
        _stories =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _stories .append (_x )

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

        return cls (count =_count ,stories =_stories ,chats =_chats ,users =_users )

class StoryViews (TLObject ):
    CONSTRUCTOR_ID =0xde9eed1d 
    SUBCLASS_OF_ID =0x4b3fc4ba 

    def __init__ (self ,views :List ['TypeStoryViews'],users :List ['TypeUser']):
        """"""
        self .views =views 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'StoryViews',
        'views':[]if self .views is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .views ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x1d\xed\x9e\xde',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .views )),b''.join (x ._bytes ()for x in self .views ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _views =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _views .append (_x )

        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        return cls (views =_views ,users =_users )

class StoryViewsList (TLObject ):
    CONSTRUCTOR_ID =0x46e9b9ec 
    SUBCLASS_OF_ID =0xb9437560 

    def __init__ (self ,count :int ,reactions_count :int ,views :List ['TypeStoryView'],users :List ['TypeUser'],next_offset :Optional [str ]=None ):
        """"""
        self .count =count 
        self .reactions_count =reactions_count 
        self .views =views 
        self .users =users 
        self .next_offset =next_offset 

    def to_dict (self ):
        return {
        '_':'StoryViewsList',
        'count':self .count ,
        'reactions_count':self .reactions_count ,
        'views':[]if self .views is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .views ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ],
        'next_offset':self .next_offset 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xec\xb9\xe9F',
        struct .pack ('<I',(0 if self .next_offset is None or self .next_offset is False else 1 )),
        struct .pack ('<i',self .count ),
        struct .pack ('<i',self .reactions_count ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .views )),b''.join (x ._bytes ()for x in self .views ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        b''if self .next_offset is None or self .next_offset is False else (self .serialize_bytes (self .next_offset )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _count =reader .read_int ()
        _reactions_count =reader .read_int ()
        reader .read_int ()
        _views =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _views .append (_x )

        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        if flags &1 :
            _next_offset =reader .tgread_string ()
        else :
            _next_offset =None 
        return cls (count =_count ,reactions_count =_reactions_count ,views =_views ,users =_users ,next_offset =_next_offset )

