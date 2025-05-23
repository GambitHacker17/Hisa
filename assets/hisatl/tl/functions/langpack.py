""""""
from ...tl .tlobject import TLObject 
from ...tl .tlobject import TLRequest 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 

class GetDifferenceRequest (TLRequest ):
    CONSTRUCTOR_ID =0xcd984aa5 
    SUBCLASS_OF_ID =0x52662d55 

    def __init__ (self ,lang_pack :str ,lang_code :str ,from_version :int ):
        """"""
        self .lang_pack =lang_pack 
        self .lang_code =lang_code 
        self .from_version =from_version 

    def to_dict (self ):
        return {
        '_':'GetDifferenceRequest',
        'lang_pack':self .lang_pack ,
        'lang_code':self .lang_code ,
        'from_version':self .from_version 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xa5J\x98\xcd',
        self .serialize_bytes (self .lang_pack ),
        self .serialize_bytes (self .lang_code ),
        struct .pack ('<i',self .from_version ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _lang_pack =reader .tgread_string ()
        _lang_code =reader .tgread_string ()
        _from_version =reader .read_int ()
        return cls (lang_pack =_lang_pack ,lang_code =_lang_code ,from_version =_from_version )

class GetLangPackRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf2f2330a 
    SUBCLASS_OF_ID =0x52662d55 

    def __init__ (self ,lang_pack :str ,lang_code :str ):
        """"""
        self .lang_pack =lang_pack 
        self .lang_code =lang_code 

    def to_dict (self ):
        return {
        '_':'GetLangPackRequest',
        'lang_pack':self .lang_pack ,
        'lang_code':self .lang_code 
        }

    def _bytes (self ):
        return b''.join ((
        b'\n3\xf2\xf2',
        self .serialize_bytes (self .lang_pack ),
        self .serialize_bytes (self .lang_code ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _lang_pack =reader .tgread_string ()
        _lang_code =reader .tgread_string ()
        return cls (lang_pack =_lang_pack ,lang_code =_lang_code )

class GetLanguageRequest (TLRequest ):
    CONSTRUCTOR_ID =0x6a596502 
    SUBCLASS_OF_ID =0xabac89b7 

    def __init__ (self ,lang_pack :str ,lang_code :str ):
        """"""
        self .lang_pack =lang_pack 
        self .lang_code =lang_code 

    def to_dict (self ):
        return {
        '_':'GetLanguageRequest',
        'lang_pack':self .lang_pack ,
        'lang_code':self .lang_code 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x02eYj',
        self .serialize_bytes (self .lang_pack ),
        self .serialize_bytes (self .lang_code ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _lang_pack =reader .tgread_string ()
        _lang_code =reader .tgread_string ()
        return cls (lang_pack =_lang_pack ,lang_code =_lang_code )

class GetLanguagesRequest (TLRequest ):
    CONSTRUCTOR_ID =0x42c6978f 
    SUBCLASS_OF_ID =0x280912c9 

    def __init__ (self ,lang_pack :str ):
        """"""
        self .lang_pack =lang_pack 

    def to_dict (self ):
        return {
        '_':'GetLanguagesRequest',
        'lang_pack':self .lang_pack 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x8f\x97\xc6B',
        self .serialize_bytes (self .lang_pack ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _lang_pack =reader .tgread_string ()
        return cls (lang_pack =_lang_pack )

class GetStringsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xefea3803 
    SUBCLASS_OF_ID =0xc7b7353d 

    def __init__ (self ,lang_pack :str ,lang_code :str ,keys :List [str ]):
        """"""
        self .lang_pack =lang_pack 
        self .lang_code =lang_code 
        self .keys =keys 

    def to_dict (self ):
        return {
        '_':'GetStringsRequest',
        'lang_pack':self .lang_pack ,
        'lang_code':self .lang_code ,
        'keys':[]if self .keys is None else self .keys [:]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x038\xea\xef',
        self .serialize_bytes (self .lang_pack ),
        self .serialize_bytes (self .lang_code ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .keys )),b''.join (self .serialize_bytes (x )for x in self .keys ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _lang_pack =reader .tgread_string ()
        _lang_code =reader .tgread_string ()
        reader .read_int ()
        _keys =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_string ()
            _keys .append (_x )

        return cls (lang_pack =_lang_pack ,lang_code =_lang_code ,keys =_keys )

