""""""
from ...tl .tlobject import TLObject 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeAccessPointRule ,TypeChat ,TypeDataJSON ,TypeDocument ,TypeJSONValue ,TypeMessageEntity ,TypePeer ,TypePremiumSubscriptionOption ,TypeRecentMeUrl ,TypeUser 
    from ...tl .types .help import TypeCountry ,TypeCountryCode ,TypeTermsOfService 

class AppConfig (TLObject ):
    CONSTRUCTOR_ID =0xdd18782e 
    SUBCLASS_OF_ID =0x14381c9a 

    def __init__ (self ,hash :int ,config :'TypeJSONValue'):
        """"""
        self .hash =hash 
        self .config =config 

    def to_dict (self ):
        return {
        '_':'AppConfig',
        'hash':self .hash ,
        'config':self .config .to_dict ()if isinstance (self .config ,TLObject )else self .config 
        }

    def _bytes (self ):
        return b''.join ((
        b'.x\x18\xdd',
        struct .pack ('<i',self .hash ),
        self .config ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_int ()
        _config =reader .tgread_object ()
        return cls (hash =_hash ,config =_config )

class AppConfigNotModified (TLObject ):
    CONSTRUCTOR_ID =0x7cde641d 
    SUBCLASS_OF_ID =0x14381c9a 

    def to_dict (self ):
        return {
        '_':'AppConfigNotModified'
        }

    def _bytes (self ):
        return b''.join ((
        b'\x1dd\xde|',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class AppUpdate (TLObject ):
    CONSTRUCTOR_ID =0xccbbce30 
    SUBCLASS_OF_ID =0x5897069e 

    def __init__ (self ,id :int ,version :str ,text :str ,entities :List ['TypeMessageEntity'],can_not_skip :Optional [bool ]=None ,document :Optional ['TypeDocument']=None ,url :Optional [str ]=None ,sticker :Optional ['TypeDocument']=None ):
        """"""
        self .id =id 
        self .version =version 
        self .text =text 
        self .entities =entities 
        self .can_not_skip =can_not_skip 
        self .document =document 
        self .url =url 
        self .sticker =sticker 

    def to_dict (self ):
        return {
        '_':'AppUpdate',
        'id':self .id ,
        'version':self .version ,
        'text':self .text ,
        'entities':[]if self .entities is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .entities ],
        'can_not_skip':self .can_not_skip ,
        'document':self .document .to_dict ()if isinstance (self .document ,TLObject )else self .document ,
        'url':self .url ,
        'sticker':self .sticker .to_dict ()if isinstance (self .sticker ,TLObject )else self .sticker 
        }

    def _bytes (self ):
        return b''.join ((
        b'0\xce\xbb\xcc',
        struct .pack ('<I',(0 if self .can_not_skip is None or self .can_not_skip is False else 1 )|(0 if self .document is None or self .document is False else 2 )|(0 if self .url is None or self .url is False else 4 )|(0 if self .sticker is None or self .sticker is False else 8 )),
        struct .pack ('<i',self .id ),
        self .serialize_bytes (self .version ),
        self .serialize_bytes (self .text ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .entities )),b''.join (x ._bytes ()for x in self .entities ),
        b''if self .document is None or self .document is False else (self .document ._bytes ()),
        b''if self .url is None or self .url is False else (self .serialize_bytes (self .url )),
        b''if self .sticker is None or self .sticker is False else (self .sticker ._bytes ()),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _can_not_skip =bool (flags &1 )
        _id =reader .read_int ()
        _version =reader .tgread_string ()
        _text =reader .tgread_string ()
        reader .read_int ()
        _entities =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _entities .append (_x )

        if flags &2 :
            _document =reader .tgread_object ()
        else :
            _document =None 
        if flags &4 :
            _url =reader .tgread_string ()
        else :
            _url =None 
        if flags &8 :
            _sticker =reader .tgread_object ()
        else :
            _sticker =None 
        return cls (id =_id ,version =_version ,text =_text ,entities =_entities ,can_not_skip =_can_not_skip ,document =_document ,url =_url ,sticker =_sticker )

class ConfigSimple (TLObject ):
    CONSTRUCTOR_ID =0x5a592a6c 
    SUBCLASS_OF_ID =0x29183ac4 

    def __init__ (self ,date :Optional [datetime ],expires :Optional [datetime ],rules :List ['TypeAccessPointRule']):
        """"""
        self .date =date 
        self .expires =expires 
        self .rules =rules 

    def to_dict (self ):
        return {
        '_':'ConfigSimple',
        'date':self .date ,
        'expires':self .expires ,
        'rules':[]if self .rules is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .rules ]
        }

    def _bytes (self ):
        return b''.join ((
        b'l*YZ',
        self .serialize_datetime (self .date ),
        self .serialize_datetime (self .expires ),
        struct .pack ('<i',len (self .rules )),b''.join (x ._bytes ()for x in self .rules ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _date =reader .tgread_date ()
        _expires =reader .tgread_date ()
        _rules =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _rules .append (_x )

        return cls (date =_date ,expires =_expires ,rules =_rules )

class CountriesList (TLObject ):
    CONSTRUCTOR_ID =0x87d0759e 
    SUBCLASS_OF_ID =0xea31fe88 

    def __init__ (self ,countries :List ['TypeCountry'],hash :int ):
        """"""
        self .countries =countries 
        self .hash =hash 

    def to_dict (self ):
        return {
        '_':'CountriesList',
        'countries':[]if self .countries is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .countries ],
        'hash':self .hash 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x9eu\xd0\x87',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .countries )),b''.join (x ._bytes ()for x in self .countries ),
        struct .pack ('<i',self .hash ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _countries =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _countries .append (_x )

        _hash =reader .read_int ()
        return cls (countries =_countries ,hash =_hash )

class CountriesListNotModified (TLObject ):
    CONSTRUCTOR_ID =0x93cc1f32 
    SUBCLASS_OF_ID =0xea31fe88 

    def to_dict (self ):
        return {
        '_':'CountriesListNotModified'
        }

    def _bytes (self ):
        return b''.join ((
        b'2\x1f\xcc\x93',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class Country (TLObject ):
    CONSTRUCTOR_ID =0xc3878e23 
    SUBCLASS_OF_ID =0xa22e9e28 

    def __init__ (self ,iso2 :str ,default_name :str ,country_codes :List ['TypeCountryCode'],hidden :Optional [bool ]=None ,name :Optional [str ]=None ):
        """"""
        self .iso2 =iso2 
        self .default_name =default_name 
        self .country_codes =country_codes 
        self .hidden =hidden 
        self .name =name 

    def to_dict (self ):
        return {
        '_':'Country',
        'iso2':self .iso2 ,
        'default_name':self .default_name ,
        'country_codes':[]if self .country_codes is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .country_codes ],
        'hidden':self .hidden ,
        'name':self .name 
        }

    def _bytes (self ):
        return b''.join ((
        b'#\x8e\x87\xc3',
        struct .pack ('<I',(0 if self .hidden is None or self .hidden is False else 1 )|(0 if self .name is None or self .name is False else 2 )),
        self .serialize_bytes (self .iso2 ),
        self .serialize_bytes (self .default_name ),
        b''if self .name is None or self .name is False else (self .serialize_bytes (self .name )),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .country_codes )),b''.join (x ._bytes ()for x in self .country_codes ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _hidden =bool (flags &1 )
        _iso2 =reader .tgread_string ()
        _default_name =reader .tgread_string ()
        if flags &2 :
            _name =reader .tgread_string ()
        else :
            _name =None 
        reader .read_int ()
        _country_codes =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _country_codes .append (_x )

        return cls (iso2 =_iso2 ,default_name =_default_name ,country_codes =_country_codes ,hidden =_hidden ,name =_name )

class CountryCode (TLObject ):
    CONSTRUCTOR_ID =0x4203c5ef 
    SUBCLASS_OF_ID =0x76f34665 

    def __init__ (self ,country_code :str ,prefixes :Optional [List [str ]]=None ,patterns :Optional [List [str ]]=None ):
        """"""
        self .country_code =country_code 
        self .prefixes =prefixes 
        self .patterns =patterns 

    def to_dict (self ):
        return {
        '_':'CountryCode',
        'country_code':self .country_code ,
        'prefixes':[]if self .prefixes is None else self .prefixes [:],
        'patterns':[]if self .patterns is None else self .patterns [:]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xef\xc5\x03B',
        struct .pack ('<I',(0 if self .prefixes is None or self .prefixes is False else 1 )|(0 if self .patterns is None or self .patterns is False else 2 )),
        self .serialize_bytes (self .country_code ),
        b''if self .prefixes is None or self .prefixes is False else b''.join ((b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .prefixes )),b''.join (self .serialize_bytes (x )for x in self .prefixes ))),
        b''if self .patterns is None or self .patterns is False else b''.join ((b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .patterns )),b''.join (self .serialize_bytes (x )for x in self .patterns ))),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _country_code =reader .tgread_string ()
        if flags &1 :
            reader .read_int ()
            _prefixes =[]
            for _ in range (reader .read_int ()):
                _x =reader .tgread_string ()
                _prefixes .append (_x )

        else :
            _prefixes =None 
        if flags &2 :
            reader .read_int ()
            _patterns =[]
            for _ in range (reader .read_int ()):
                _x =reader .tgread_string ()
                _patterns .append (_x )

        else :
            _patterns =None 
        return cls (country_code =_country_code ,prefixes =_prefixes ,patterns =_patterns )

class DeepLinkInfo (TLObject ):
    CONSTRUCTOR_ID =0x6a4ee832 
    SUBCLASS_OF_ID =0x984aac38 

    def __init__ (self ,message :str ,update_app :Optional [bool ]=None ,entities :Optional [List ['TypeMessageEntity']]=None ):
        """"""
        self .message =message 
        self .update_app =update_app 
        self .entities =entities 

    def to_dict (self ):
        return {
        '_':'DeepLinkInfo',
        'message':self .message ,
        'update_app':self .update_app ,
        'entities':[]if self .entities is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .entities ]
        }

    def _bytes (self ):
        return b''.join ((
        b'2\xe8Nj',
        struct .pack ('<I',(0 if self .update_app is None or self .update_app is False else 1 )|(0 if self .entities is None or self .entities is False else 2 )),
        self .serialize_bytes (self .message ),
        b''if self .entities is None or self .entities is False else b''.join ((b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .entities )),b''.join (x ._bytes ()for x in self .entities ))),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _update_app =bool (flags &1 )
        _message =reader .tgread_string ()
        if flags &2 :
            reader .read_int ()
            _entities =[]
            for _ in range (reader .read_int ()):
                _x =reader .tgread_object ()
                _entities .append (_x )

        else :
            _entities =None 
        return cls (message =_message ,update_app =_update_app ,entities =_entities )

class DeepLinkInfoEmpty (TLObject ):
    CONSTRUCTOR_ID =0x66afa166 
    SUBCLASS_OF_ID =0x984aac38 

    def to_dict (self ):
        return {
        '_':'DeepLinkInfoEmpty'
        }

    def _bytes (self ):
        return b''.join ((
        b'f\xa1\xaff',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class InviteText (TLObject ):
    CONSTRUCTOR_ID =0x18cb9f78 
    SUBCLASS_OF_ID =0xcf70aa35 

    def __init__ (self ,message :str ):
        """"""
        self .message =message 

    def to_dict (self ):
        return {
        '_':'InviteText',
        'message':self .message 
        }

    def _bytes (self ):
        return b''.join ((
        b'x\x9f\xcb\x18',
        self .serialize_bytes (self .message ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _message =reader .tgread_string ()
        return cls (message =_message )

class NoAppUpdate (TLObject ):
    CONSTRUCTOR_ID =0xc45a6536 
    SUBCLASS_OF_ID =0x5897069e 

    def to_dict (self ):
        return {
        '_':'NoAppUpdate'
        }

    def _bytes (self ):
        return b''.join ((
        b'6eZ\xc4',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class PassportConfig (TLObject ):
    CONSTRUCTOR_ID =0xa098d6af 
    SUBCLASS_OF_ID =0xc666c0ad 

    def __init__ (self ,hash :int ,countries_langs :'TypeDataJSON'):
        """"""
        self .hash =hash 
        self .countries_langs =countries_langs 

    def to_dict (self ):
        return {
        '_':'PassportConfig',
        'hash':self .hash ,
        'countries_langs':self .countries_langs .to_dict ()if isinstance (self .countries_langs ,TLObject )else self .countries_langs 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xaf\xd6\x98\xa0',
        struct .pack ('<i',self .hash ),
        self .countries_langs ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_int ()
        _countries_langs =reader .tgread_object ()
        return cls (hash =_hash ,countries_langs =_countries_langs )

class PassportConfigNotModified (TLObject ):
    CONSTRUCTOR_ID =0xbfb9f457 
    SUBCLASS_OF_ID =0xc666c0ad 

    def to_dict (self ):
        return {
        '_':'PassportConfigNotModified'
        }

    def _bytes (self ):
        return b''.join ((
        b'W\xf4\xb9\xbf',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class PremiumPromo (TLObject ):
    CONSTRUCTOR_ID =0x5334759c 
    SUBCLASS_OF_ID =0xc987a338 

    def __init__ (self ,status_text :str ,status_entities :List ['TypeMessageEntity'],video_sections :List [str ],videos :List ['TypeDocument'],period_options :List ['TypePremiumSubscriptionOption'],users :List ['TypeUser']):
        """"""
        self .status_text =status_text 
        self .status_entities =status_entities 
        self .video_sections =video_sections 
        self .videos =videos 
        self .period_options =period_options 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'PremiumPromo',
        'status_text':self .status_text ,
        'status_entities':[]if self .status_entities is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .status_entities ],
        'video_sections':[]if self .video_sections is None else self .video_sections [:],
        'videos':[]if self .videos is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .videos ],
        'period_options':[]if self .period_options is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .period_options ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x9cu4S',
        self .serialize_bytes (self .status_text ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .status_entities )),b''.join (x ._bytes ()for x in self .status_entities ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .video_sections )),b''.join (self .serialize_bytes (x )for x in self .video_sections ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .videos )),b''.join (x ._bytes ()for x in self .videos ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .period_options )),b''.join (x ._bytes ()for x in self .period_options ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _status_text =reader .tgread_string ()
        reader .read_int ()
        _status_entities =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _status_entities .append (_x )

        reader .read_int ()
        _video_sections =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_string ()
            _video_sections .append (_x )

        reader .read_int ()
        _videos =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _videos .append (_x )

        reader .read_int ()
        _period_options =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _period_options .append (_x )

        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        return cls (status_text =_status_text ,status_entities =_status_entities ,video_sections =_video_sections ,videos =_videos ,period_options =_period_options ,users =_users )

class PromoData (TLObject ):
    CONSTRUCTOR_ID =0x8c39793f 
    SUBCLASS_OF_ID =0x9d595542 

    def __init__ (self ,expires :Optional [datetime ],peer :'TypePeer',chats :List ['TypeChat'],users :List ['TypeUser'],proxy :Optional [bool ]=None ,psa_type :Optional [str ]=None ,psa_message :Optional [str ]=None ):
        """"""
        self .expires =expires 
        self .peer =peer 
        self .chats =chats 
        self .users =users 
        self .proxy =proxy 
        self .psa_type =psa_type 
        self .psa_message =psa_message 

    def to_dict (self ):
        return {
        '_':'PromoData',
        'expires':self .expires ,
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ],
        'proxy':self .proxy ,
        'psa_type':self .psa_type ,
        'psa_message':self .psa_message 
        }

    def _bytes (self ):
        return b''.join ((
        b'?y9\x8c',
        struct .pack ('<I',(0 if self .proxy is None or self .proxy is False else 1 )|(0 if self .psa_type is None or self .psa_type is False else 2 )|(0 if self .psa_message is None or self .psa_message is False else 4 )),
        self .serialize_datetime (self .expires ),
        self .peer ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        b''if self .psa_type is None or self .psa_type is False else (self .serialize_bytes (self .psa_type )),
        b''if self .psa_message is None or self .psa_message is False else (self .serialize_bytes (self .psa_message )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _proxy =bool (flags &1 )
        _expires =reader .tgread_date ()
        _peer =reader .tgread_object ()
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

        if flags &2 :
            _psa_type =reader .tgread_string ()
        else :
            _psa_type =None 
        if flags &4 :
            _psa_message =reader .tgread_string ()
        else :
            _psa_message =None 
        return cls (expires =_expires ,peer =_peer ,chats =_chats ,users =_users ,proxy =_proxy ,psa_type =_psa_type ,psa_message =_psa_message )

class PromoDataEmpty (TLObject ):
    CONSTRUCTOR_ID =0x98f6ac75 
    SUBCLASS_OF_ID =0x9d595542 

    def __init__ (self ,expires :Optional [datetime ]):
        """"""
        self .expires =expires 

    def to_dict (self ):
        return {
        '_':'PromoDataEmpty',
        'expires':self .expires 
        }

    def _bytes (self ):
        return b''.join ((
        b'u\xac\xf6\x98',
        self .serialize_datetime (self .expires ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _expires =reader .tgread_date ()
        return cls (expires =_expires )

class RecentMeUrls (TLObject ):
    CONSTRUCTOR_ID =0xe0310d7 
    SUBCLASS_OF_ID =0xf269c477 

    def __init__ (self ,urls :List ['TypeRecentMeUrl'],chats :List ['TypeChat'],users :List ['TypeUser']):
        """"""
        self .urls =urls 
        self .chats =chats 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'RecentMeUrls',
        'urls':[]if self .urls is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .urls ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xd7\x10\x03\x0e',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .urls )),b''.join (x ._bytes ()for x in self .urls ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _urls =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _urls .append (_x )

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

        return cls (urls =_urls ,chats =_chats ,users =_users )

class Support (TLObject ):
    CONSTRUCTOR_ID =0x17c6b5f6 
    SUBCLASS_OF_ID =0x7159bceb 

    def __init__ (self ,phone_number :str ,user :'TypeUser'):
        """"""
        self .phone_number =phone_number 
        self .user =user 

    def to_dict (self ):
        return {
        '_':'Support',
        'phone_number':self .phone_number ,
        'user':self .user .to_dict ()if isinstance (self .user ,TLObject )else self .user 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf6\xb5\xc6\x17',
        self .serialize_bytes (self .phone_number ),
        self .user ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _phone_number =reader .tgread_string ()
        _user =reader .tgread_object ()
        return cls (phone_number =_phone_number ,user =_user )

class SupportName (TLObject ):
    CONSTRUCTOR_ID =0x8c05f1c9 
    SUBCLASS_OF_ID =0x7f50b7c2 

    def __init__ (self ,name :str ):
        """"""
        self .name =name 

    def to_dict (self ):
        return {
        '_':'SupportName',
        'name':self .name 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc9\xf1\x05\x8c',
        self .serialize_bytes (self .name ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _name =reader .tgread_string ()
        return cls (name =_name )

class TermsOfService (TLObject ):
    CONSTRUCTOR_ID =0x780a0310 
    SUBCLASS_OF_ID =0x20ee8312 

    def __init__ (self ,id :'TypeDataJSON',text :str ,entities :List ['TypeMessageEntity'],popup :Optional [bool ]=None ,min_age_confirm :Optional [int ]=None ):
        """"""
        self .id =id 
        self .text =text 
        self .entities =entities 
        self .popup =popup 
        self .min_age_confirm =min_age_confirm 

    def to_dict (self ):
        return {
        '_':'TermsOfService',
        'id':self .id .to_dict ()if isinstance (self .id ,TLObject )else self .id ,
        'text':self .text ,
        'entities':[]if self .entities is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .entities ],
        'popup':self .popup ,
        'min_age_confirm':self .min_age_confirm 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x10\x03\nx',
        struct .pack ('<I',(0 if self .popup is None or self .popup is False else 1 )|(0 if self .min_age_confirm is None or self .min_age_confirm is False else 2 )),
        self .id ._bytes (),
        self .serialize_bytes (self .text ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .entities )),b''.join (x ._bytes ()for x in self .entities ),
        b''if self .min_age_confirm is None or self .min_age_confirm is False else (struct .pack ('<i',self .min_age_confirm )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _popup =bool (flags &1 )
        _id =reader .tgread_object ()
        _text =reader .tgread_string ()
        reader .read_int ()
        _entities =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _entities .append (_x )

        if flags &2 :
            _min_age_confirm =reader .read_int ()
        else :
            _min_age_confirm =None 
        return cls (id =_id ,text =_text ,entities =_entities ,popup =_popup ,min_age_confirm =_min_age_confirm )

class TermsOfServiceUpdate (TLObject ):
    CONSTRUCTOR_ID =0x28ecf961 
    SUBCLASS_OF_ID =0x293c2977 

    def __init__ (self ,expires :Optional [datetime ],terms_of_service :'TypeTermsOfService'):
        """"""
        self .expires =expires 
        self .terms_of_service =terms_of_service 

    def to_dict (self ):
        return {
        '_':'TermsOfServiceUpdate',
        'expires':self .expires ,
        'terms_of_service':self .terms_of_service .to_dict ()if isinstance (self .terms_of_service ,TLObject )else self .terms_of_service 
        }

    def _bytes (self ):
        return b''.join ((
        b'a\xf9\xec(',
        self .serialize_datetime (self .expires ),
        self .terms_of_service ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _expires =reader .tgread_date ()
        _terms_of_service =reader .tgread_object ()
        return cls (expires =_expires ,terms_of_service =_terms_of_service )

class TermsOfServiceUpdateEmpty (TLObject ):
    CONSTRUCTOR_ID =0xe3309f7f 
    SUBCLASS_OF_ID =0x293c2977 

    def __init__ (self ,expires :Optional [datetime ]):
        """"""
        self .expires =expires 

    def to_dict (self ):
        return {
        '_':'TermsOfServiceUpdateEmpty',
        'expires':self .expires 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x7f\x9f0\xe3',
        self .serialize_datetime (self .expires ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _expires =reader .tgread_date ()
        return cls (expires =_expires )

class UserInfo (TLObject ):
    CONSTRUCTOR_ID =0x1eb3758 
    SUBCLASS_OF_ID =0x5c53d7d8 

    def __init__ (self ,message :str ,entities :List ['TypeMessageEntity'],author :str ,date :Optional [datetime ]):
        """"""
        self .message =message 
        self .entities =entities 
        self .author =author 
        self .date =date 

    def to_dict (self ):
        return {
        '_':'UserInfo',
        'message':self .message ,
        'entities':[]if self .entities is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .entities ],
        'author':self .author ,
        'date':self .date 
        }

    def _bytes (self ):
        return b''.join ((
        b'X7\xeb\x01',
        self .serialize_bytes (self .message ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .entities )),b''.join (x ._bytes ()for x in self .entities ),
        self .serialize_bytes (self .author ),
        self .serialize_datetime (self .date ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _message =reader .tgread_string ()
        reader .read_int ()
        _entities =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _entities .append (_x )

        _author =reader .tgread_string ()
        _date =reader .tgread_date ()
        return cls (message =_message ,entities =_entities ,author =_author ,date =_date )

class UserInfoEmpty (TLObject ):
    CONSTRUCTOR_ID =0xf3ae2eed 
    SUBCLASS_OF_ID =0x5c53d7d8 

    def to_dict (self ):
        return {
        '_':'UserInfoEmpty'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xed.\xae\xf3',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

