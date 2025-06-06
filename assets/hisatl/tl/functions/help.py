""""""
from ...tl .tlobject import TLObject 
from ...tl .tlobject import TLRequest 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeDataJSON ,TypeInputAppEvent ,TypeInputPeer ,TypeInputUser ,TypeMessageEntity 

class AcceptTermsOfServiceRequest (TLRequest ):
    CONSTRUCTOR_ID =0xee72f79a 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,id :'TypeDataJSON'):
        """"""
        self .id =id 

    def to_dict (self ):
        return {
        '_':'AcceptTermsOfServiceRequest',
        'id':self .id .to_dict ()if isinstance (self .id ,TLObject )else self .id 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x9a\xf7r\xee',
        self .id ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _id =reader .tgread_object ()
        return cls (id =_id )

class DismissSuggestionRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf50dbaa1 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,peer :'TypeInputPeer',suggestion :str ):
        """"""
        self .peer =peer 
        self .suggestion =suggestion 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'DismissSuggestionRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'suggestion':self .suggestion 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xa1\xba\r\xf5',
        self .peer ._bytes (),
        self .serialize_bytes (self .suggestion ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        _suggestion =reader .tgread_string ()
        return cls (peer =_peer ,suggestion =_suggestion )

class EditUserInfoRequest (TLRequest ):
    CONSTRUCTOR_ID =0x66b91b70 
    SUBCLASS_OF_ID =0x5c53d7d8 

    def __init__ (self ,user_id :'TypeInputUser',message :str ,entities :List ['TypeMessageEntity']):
        """"""
        self .user_id =user_id 
        self .message =message 
        self .entities =entities 

    async def resolve (self ,client ,utils ):
        self .user_id =utils .get_input_user (await client .get_input_entity (self .user_id ))

    def to_dict (self ):
        return {
        '_':'EditUserInfoRequest',
        'user_id':self .user_id .to_dict ()if isinstance (self .user_id ,TLObject )else self .user_id ,
        'message':self .message ,
        'entities':[]if self .entities is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .entities ]
        }

    def _bytes (self ):
        return b''.join ((
        b'p\x1b\xb9f',
        self .user_id ._bytes (),
        self .serialize_bytes (self .message ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .entities )),b''.join (x ._bytes ()for x in self .entities ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _user_id =reader .tgread_object ()
        _message =reader .tgread_string ()
        reader .read_int ()
        _entities =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _entities .append (_x )

        return cls (user_id =_user_id ,message =_message ,entities =_entities )

class GetAppChangelogRequest (TLRequest ):
    CONSTRUCTOR_ID =0x9010ef6f 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,prev_app_version :str ):
        """"""
        self .prev_app_version =prev_app_version 

    def to_dict (self ):
        return {
        '_':'GetAppChangelogRequest',
        'prev_app_version':self .prev_app_version 
        }

    def _bytes (self ):
        return b''.join ((
        b'o\xef\x10\x90',
        self .serialize_bytes (self .prev_app_version ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _prev_app_version =reader .tgread_string ()
        return cls (prev_app_version =_prev_app_version )

class GetAppConfigRequest (TLRequest ):
    CONSTRUCTOR_ID =0x61e3f854 
    SUBCLASS_OF_ID =0x14381c9a 

    def __init__ (self ,hash :int ):
        """"""
        self .hash =hash 

    def to_dict (self ):
        return {
        '_':'GetAppConfigRequest',
        'hash':self .hash 
        }

    def _bytes (self ):
        return b''.join ((
        b'T\xf8\xe3a',
        struct .pack ('<i',self .hash ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_int ()
        return cls (hash =_hash )

class GetAppUpdateRequest (TLRequest ):
    CONSTRUCTOR_ID =0x522d5a7d 
    SUBCLASS_OF_ID =0x5897069e 

    def __init__ (self ,source :str ):
        """"""
        self .source =source 

    def to_dict (self ):
        return {
        '_':'GetAppUpdateRequest',
        'source':self .source 
        }

    def _bytes (self ):
        return b''.join ((
        b'}Z-R',
        self .serialize_bytes (self .source ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _source =reader .tgread_string ()
        return cls (source =_source )

class GetCdnConfigRequest (TLRequest ):
    CONSTRUCTOR_ID =0x52029342 
    SUBCLASS_OF_ID =0xecda397c 

    def to_dict (self ):
        return {
        '_':'GetCdnConfigRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'B\x93\x02R',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetConfigRequest (TLRequest ):
    CONSTRUCTOR_ID =0xc4f9186b 
    SUBCLASS_OF_ID =0xd3262a4a 

    def to_dict (self ):
        return {
        '_':'GetConfigRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'k\x18\xf9\xc4',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetCountriesListRequest (TLRequest ):
    CONSTRUCTOR_ID =0x735787a8 
    SUBCLASS_OF_ID =0xea31fe88 

    def __init__ (self ,lang_code :str ,hash :int ):
        """"""
        self .lang_code =lang_code 
        self .hash =hash 

    def to_dict (self ):
        return {
        '_':'GetCountriesListRequest',
        'lang_code':self .lang_code ,
        'hash':self .hash 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xa8\x87Ws',
        self .serialize_bytes (self .lang_code ),
        struct .pack ('<i',self .hash ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _lang_code =reader .tgread_string ()
        _hash =reader .read_int ()
        return cls (lang_code =_lang_code ,hash =_hash )

class GetDeepLinkInfoRequest (TLRequest ):
    CONSTRUCTOR_ID =0x3fedc75f 
    SUBCLASS_OF_ID =0x984aac38 

    def __init__ (self ,path :str ):
        """"""
        self .path =path 

    def to_dict (self ):
        return {
        '_':'GetDeepLinkInfoRequest',
        'path':self .path 
        }

    def _bytes (self ):
        return b''.join ((
        b'_\xc7\xed?',
        self .serialize_bytes (self .path ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _path =reader .tgread_string ()
        return cls (path =_path )

class GetInviteTextRequest (TLRequest ):
    CONSTRUCTOR_ID =0x4d392343 
    SUBCLASS_OF_ID =0xcf70aa35 

    def to_dict (self ):
        return {
        '_':'GetInviteTextRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'C#9M',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetNearestDcRequest (TLRequest ):
    CONSTRUCTOR_ID =0x1fb33026 
    SUBCLASS_OF_ID =0x3877045f 

    def to_dict (self ):
        return {
        '_':'GetNearestDcRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'&0\xb3\x1f',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetPassportConfigRequest (TLRequest ):
    CONSTRUCTOR_ID =0xc661ad08 
    SUBCLASS_OF_ID =0xc666c0ad 

    def __init__ (self ,hash :int ):
        """"""
        self .hash =hash 

    def to_dict (self ):
        return {
        '_':'GetPassportConfigRequest',
        'hash':self .hash 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x08\xada\xc6',
        struct .pack ('<i',self .hash ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_int ()
        return cls (hash =_hash )

class GetPremiumPromoRequest (TLRequest ):
    CONSTRUCTOR_ID =0xb81b93d4 
    SUBCLASS_OF_ID =0xc987a338 

    def to_dict (self ):
        return {
        '_':'GetPremiumPromoRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xd4\x93\x1b\xb8',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetPromoDataRequest (TLRequest ):
    CONSTRUCTOR_ID =0xc0977421 
    SUBCLASS_OF_ID =0x9d595542 

    def to_dict (self ):
        return {
        '_':'GetPromoDataRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'!t\x97\xc0',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetRecentMeUrlsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x3dc0f114 
    SUBCLASS_OF_ID =0xf269c477 

    def __init__ (self ,referer :str ):
        """"""
        self .referer =referer 

    def to_dict (self ):
        return {
        '_':'GetRecentMeUrlsRequest',
        'referer':self .referer 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x14\xf1\xc0=',
        self .serialize_bytes (self .referer ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _referer =reader .tgread_string ()
        return cls (referer =_referer )

class GetSupportRequest (TLRequest ):
    CONSTRUCTOR_ID =0x9cdf08cd 
    SUBCLASS_OF_ID =0x7159bceb 

    def to_dict (self ):
        return {
        '_':'GetSupportRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xcd\x08\xdf\x9c',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetSupportNameRequest (TLRequest ):
    CONSTRUCTOR_ID =0xd360e72c 
    SUBCLASS_OF_ID =0x7f50b7c2 

    def to_dict (self ):
        return {
        '_':'GetSupportNameRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b',\xe7`\xd3',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetTermsOfServiceUpdateRequest (TLRequest ):
    CONSTRUCTOR_ID =0x2ca51fd1 
    SUBCLASS_OF_ID =0x293c2977 

    def to_dict (self ):
        return {
        '_':'GetTermsOfServiceUpdateRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xd1\x1f\xa5,',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetUserInfoRequest (TLRequest ):
    CONSTRUCTOR_ID =0x38a08d3 
    SUBCLASS_OF_ID =0x5c53d7d8 

    def __init__ (self ,user_id :'TypeInputUser'):
        """"""
        self .user_id =user_id 

    async def resolve (self ,client ,utils ):
        self .user_id =utils .get_input_user (await client .get_input_entity (self .user_id ))

    def to_dict (self ):
        return {
        '_':'GetUserInfoRequest',
        'user_id':self .user_id .to_dict ()if isinstance (self .user_id ,TLObject )else self .user_id 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xd3\x08\x8a\x03',
        self .user_id ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _user_id =reader .tgread_object ()
        return cls (user_id =_user_id )

class HidePromoDataRequest (TLRequest ):
    CONSTRUCTOR_ID =0x1e251c95 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,peer :'TypeInputPeer'):
        """"""
        self .peer =peer 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'HidePromoDataRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x95\x1c%\x1e',
        self .peer ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        return cls (peer =_peer )

class SaveAppLogRequest (TLRequest ):
    CONSTRUCTOR_ID =0x6f02f748 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,events :List ['TypeInputAppEvent']):
        """"""
        self .events =events 

    def to_dict (self ):
        return {
        '_':'SaveAppLogRequest',
        'events':[]if self .events is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .events ]
        }

    def _bytes (self ):
        return b''.join ((
        b'H\xf7\x02o',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .events )),b''.join (x ._bytes ()for x in self .events ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _events =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _events .append (_x )

        return cls (events =_events )

class SetBotUpdatesStatusRequest (TLRequest ):
    CONSTRUCTOR_ID =0xec22cfcd 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,pending_updates_count :int ,message :str ):
        """"""
        self .pending_updates_count =pending_updates_count 
        self .message =message 

    def to_dict (self ):
        return {
        '_':'SetBotUpdatesStatusRequest',
        'pending_updates_count':self .pending_updates_count ,
        'message':self .message 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xcd\xcf"\xec',
        struct .pack ('<i',self .pending_updates_count ),
        self .serialize_bytes (self .message ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _pending_updates_count =reader .read_int ()
        _message =reader .tgread_string ()
        return cls (pending_updates_count =_pending_updates_count ,message =_message )

