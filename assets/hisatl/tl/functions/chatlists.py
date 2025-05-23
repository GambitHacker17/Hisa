""""""
from ...tl .tlobject import TLObject 
from ...tl .tlobject import TLRequest 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeInputChatlist ,TypeInputPeer 

class CheckChatlistInviteRequest (TLRequest ):
    CONSTRUCTOR_ID =0x41c10fff 
    SUBCLASS_OF_ID =0x41720e75 

    def __init__ (self ,slug :str ):
        """"""
        self .slug =slug 

    def to_dict (self ):
        return {
        '_':'CheckChatlistInviteRequest',
        'slug':self .slug 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xff\x0f\xc1A',
        self .serialize_bytes (self .slug ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _slug =reader .tgread_string ()
        return cls (slug =_slug )

class DeleteExportedInviteRequest (TLRequest ):
    CONSTRUCTOR_ID =0x719c5c5e 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,chatlist :'TypeInputChatlist',slug :str ):
        """"""
        self .chatlist =chatlist 
        self .slug =slug 

    def to_dict (self ):
        return {
        '_':'DeleteExportedInviteRequest',
        'chatlist':self .chatlist .to_dict ()if isinstance (self .chatlist ,TLObject )else self .chatlist ,
        'slug':self .slug 
        }

    def _bytes (self ):
        return b''.join ((
        b'^\\\x9cq',
        self .chatlist ._bytes (),
        self .serialize_bytes (self .slug ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _chatlist =reader .tgread_object ()
        _slug =reader .tgread_string ()
        return cls (chatlist =_chatlist ,slug =_slug )

class EditExportedInviteRequest (TLRequest ):
    CONSTRUCTOR_ID =0x653db63d 
    SUBCLASS_OF_ID =0x7711f8ff 

    def __init__ (self ,chatlist :'TypeInputChatlist',slug :str ,title :Optional [str ]=None ,peers :Optional [List ['TypeInputPeer']]=None ):
        """"""
        self .chatlist =chatlist 
        self .slug =slug 
        self .title =title 
        self .peers =peers 

    async def resolve (self ,client ,utils ):
        if self .peers :
            _tmp =[]
            for _x in self .peers :
                _tmp .append (utils .get_input_peer (await client .get_input_entity (_x )))

            self .peers =_tmp 

    def to_dict (self ):
        return {
        '_':'EditExportedInviteRequest',
        'chatlist':self .chatlist .to_dict ()if isinstance (self .chatlist ,TLObject )else self .chatlist ,
        'slug':self .slug ,
        'title':self .title ,
        'peers':[]if self .peers is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .peers ]
        }

    def _bytes (self ):
        return b''.join ((
        b'=\xb6=e',
        struct .pack ('<I',(0 if self .title is None or self .title is False else 2 )|(0 if self .peers is None or self .peers is False else 4 )),
        self .chatlist ._bytes (),
        self .serialize_bytes (self .slug ),
        b''if self .title is None or self .title is False else (self .serialize_bytes (self .title )),
        b''if self .peers is None or self .peers is False else b''.join ((b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .peers )),b''.join (x ._bytes ()for x in self .peers ))),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _chatlist =reader .tgread_object ()
        _slug =reader .tgread_string ()
        if flags &2 :
            _title =reader .tgread_string ()
        else :
            _title =None 
        if flags &4 :
            reader .read_int ()
            _peers =[]
            for _ in range (reader .read_int ()):
                _x =reader .tgread_object ()
                _peers .append (_x )

        else :
            _peers =None 
        return cls (chatlist =_chatlist ,slug =_slug ,title =_title ,peers =_peers )

class ExportChatlistInviteRequest (TLRequest ):
    CONSTRUCTOR_ID =0x8472478e 
    SUBCLASS_OF_ID =0xc2694ee9 

    def __init__ (self ,chatlist :'TypeInputChatlist',title :str ,peers :List ['TypeInputPeer']):
        """"""
        self .chatlist =chatlist 
        self .title =title 
        self .peers =peers 

    async def resolve (self ,client ,utils ):
        _tmp =[]
        for _x in self .peers :
            _tmp .append (utils .get_input_peer (await client .get_input_entity (_x )))

        self .peers =_tmp 

    def to_dict (self ):
        return {
        '_':'ExportChatlistInviteRequest',
        'chatlist':self .chatlist .to_dict ()if isinstance (self .chatlist ,TLObject )else self .chatlist ,
        'title':self .title ,
        'peers':[]if self .peers is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .peers ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x8eGr\x84',
        self .chatlist ._bytes (),
        self .serialize_bytes (self .title ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .peers )),b''.join (x ._bytes ()for x in self .peers ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _chatlist =reader .tgread_object ()
        _title =reader .tgread_string ()
        reader .read_int ()
        _peers =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _peers .append (_x )

        return cls (chatlist =_chatlist ,title =_title ,peers =_peers )

class GetChatlistUpdatesRequest (TLRequest ):
    CONSTRUCTOR_ID =0x89419521 
    SUBCLASS_OF_ID =0x7d1641ea 

    def __init__ (self ,chatlist :'TypeInputChatlist'):
        """"""
        self .chatlist =chatlist 

    def to_dict (self ):
        return {
        '_':'GetChatlistUpdatesRequest',
        'chatlist':self .chatlist .to_dict ()if isinstance (self .chatlist ,TLObject )else self .chatlist 
        }

    def _bytes (self ):
        return b''.join ((
        b'!\x95A\x89',
        self .chatlist ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _chatlist =reader .tgread_object ()
        return cls (chatlist =_chatlist )

class GetExportedInvitesRequest (TLRequest ):
    CONSTRUCTOR_ID =0xce03da83 
    SUBCLASS_OF_ID =0xe6c209c0 

    def __init__ (self ,chatlist :'TypeInputChatlist'):
        """"""
        self .chatlist =chatlist 

    def to_dict (self ):
        return {
        '_':'GetExportedInvitesRequest',
        'chatlist':self .chatlist .to_dict ()if isinstance (self .chatlist ,TLObject )else self .chatlist 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x83\xda\x03\xce',
        self .chatlist ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _chatlist =reader .tgread_object ()
        return cls (chatlist =_chatlist )

class GetLeaveChatlistSuggestionsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xfdbcd714 
    SUBCLASS_OF_ID =0xb9945d7e 

    def __init__ (self ,chatlist :'TypeInputChatlist'):
        """"""
        self .chatlist =chatlist 

    def to_dict (self ):
        return {
        '_':'GetLeaveChatlistSuggestionsRequest',
        'chatlist':self .chatlist .to_dict ()if isinstance (self .chatlist ,TLObject )else self .chatlist 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x14\xd7\xbc\xfd',
        self .chatlist ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _chatlist =reader .tgread_object ()
        return cls (chatlist =_chatlist )

class HideChatlistUpdatesRequest (TLRequest ):
    CONSTRUCTOR_ID =0x66e486fb 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,chatlist :'TypeInputChatlist'):
        """"""
        self .chatlist =chatlist 

    def to_dict (self ):
        return {
        '_':'HideChatlistUpdatesRequest',
        'chatlist':self .chatlist .to_dict ()if isinstance (self .chatlist ,TLObject )else self .chatlist 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xfb\x86\xe4f',
        self .chatlist ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _chatlist =reader .tgread_object ()
        return cls (chatlist =_chatlist )

class JoinChatlistInviteRequest (TLRequest ):
    CONSTRUCTOR_ID =0xa6b1e39a 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,slug :str ,peers :List ['TypeInputPeer']):
        """"""
        self .slug =slug 
        self .peers =peers 

    async def resolve (self ,client ,utils ):
        _tmp =[]
        for _x in self .peers :
            _tmp .append (utils .get_input_peer (await client .get_input_entity (_x )))

        self .peers =_tmp 

    def to_dict (self ):
        return {
        '_':'JoinChatlistInviteRequest',
        'slug':self .slug ,
        'peers':[]if self .peers is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .peers ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x9a\xe3\xb1\xa6',
        self .serialize_bytes (self .slug ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .peers )),b''.join (x ._bytes ()for x in self .peers ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _slug =reader .tgread_string ()
        reader .read_int ()
        _peers =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _peers .append (_x )

        return cls (slug =_slug ,peers =_peers )

class JoinChatlistUpdatesRequest (TLRequest ):
    CONSTRUCTOR_ID =0xe089f8f5 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,chatlist :'TypeInputChatlist',peers :List ['TypeInputPeer']):
        """"""
        self .chatlist =chatlist 
        self .peers =peers 

    async def resolve (self ,client ,utils ):
        _tmp =[]
        for _x in self .peers :
            _tmp .append (utils .get_input_peer (await client .get_input_entity (_x )))

        self .peers =_tmp 

    def to_dict (self ):
        return {
        '_':'JoinChatlistUpdatesRequest',
        'chatlist':self .chatlist .to_dict ()if isinstance (self .chatlist ,TLObject )else self .chatlist ,
        'peers':[]if self .peers is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .peers ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf5\xf8\x89\xe0',
        self .chatlist ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .peers )),b''.join (x ._bytes ()for x in self .peers ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _chatlist =reader .tgread_object ()
        reader .read_int ()
        _peers =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _peers .append (_x )

        return cls (chatlist =_chatlist ,peers =_peers )

class LeaveChatlistRequest (TLRequest ):
    CONSTRUCTOR_ID =0x74fae13a 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,chatlist :'TypeInputChatlist',peers :List ['TypeInputPeer']):
        """"""
        self .chatlist =chatlist 
        self .peers =peers 

    async def resolve (self ,client ,utils ):
        _tmp =[]
        for _x in self .peers :
            _tmp .append (utils .get_input_peer (await client .get_input_entity (_x )))

        self .peers =_tmp 

    def to_dict (self ):
        return {
        '_':'LeaveChatlistRequest',
        'chatlist':self .chatlist .to_dict ()if isinstance (self .chatlist ,TLObject )else self .chatlist ,
        'peers':[]if self .peers is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .peers ]
        }

    def _bytes (self ):
        return b''.join ((
        b':\xe1\xfat',
        self .chatlist ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .peers )),b''.join (x ._bytes ()for x in self .peers ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _chatlist =reader .tgread_object ()
        reader .read_int ()
        _peers =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _peers .append (_x )

        return cls (chatlist =_chatlist ,peers =_peers )

