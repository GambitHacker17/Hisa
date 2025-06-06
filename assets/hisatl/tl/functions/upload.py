""""""
from ...tl .tlobject import TLObject 
from ...tl .tlobject import TLRequest 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeInputFileLocation ,TypeInputWebFileLocation 

class GetCdnFileRequest (TLRequest ):
    CONSTRUCTOR_ID =0x395f69da 
    SUBCLASS_OF_ID =0xf5ccf928 

    def __init__ (self ,file_token :bytes ,offset :int ,limit :int ):
        """"""
        self .file_token =file_token 
        self .offset =offset 
        self .limit =limit 

    def to_dict (self ):
        return {
        '_':'GetCdnFileRequest',
        'file_token':self .file_token ,
        'offset':self .offset ,
        'limit':self .limit 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xdai_9',
        self .serialize_bytes (self .file_token ),
        struct .pack ('<q',self .offset ),
        struct .pack ('<i',self .limit ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _file_token =reader .tgread_bytes ()
        _offset =reader .read_long ()
        _limit =reader .read_int ()
        return cls (file_token =_file_token ,offset =_offset ,limit =_limit )

class GetCdnFileHashesRequest (TLRequest ):
    CONSTRUCTOR_ID =0x91dc3f31 
    SUBCLASS_OF_ID =0xa5940726 

    def __init__ (self ,file_token :bytes ,offset :int ):
        """"""
        self .file_token =file_token 
        self .offset =offset 

    def to_dict (self ):
        return {
        '_':'GetCdnFileHashesRequest',
        'file_token':self .file_token ,
        'offset':self .offset 
        }

    def _bytes (self ):
        return b''.join ((
        b'1?\xdc\x91',
        self .serialize_bytes (self .file_token ),
        struct .pack ('<q',self .offset ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _file_token =reader .tgread_bytes ()
        _offset =reader .read_long ()
        return cls (file_token =_file_token ,offset =_offset )

class GetFileRequest (TLRequest ):
    CONSTRUCTOR_ID =0xbe5335be 
    SUBCLASS_OF_ID =0x6c9bd728 

    def __init__ (self ,location :'TypeInputFileLocation',offset :int ,limit :int ,precise :Optional [bool ]=None ,cdn_supported :Optional [bool ]=None ):
        """"""
        self .location =location 
        self .offset =offset 
        self .limit =limit 
        self .precise =precise 
        self .cdn_supported =cdn_supported 

    def to_dict (self ):
        return {
        '_':'GetFileRequest',
        'location':self .location .to_dict ()if isinstance (self .location ,TLObject )else self .location ,
        'offset':self .offset ,
        'limit':self .limit ,
        'precise':self .precise ,
        'cdn_supported':self .cdn_supported 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xbe5S\xbe',
        struct .pack ('<I',(0 if self .precise is None or self .precise is False else 1 )|(0 if self .cdn_supported is None or self .cdn_supported is False else 2 )),
        self .location ._bytes (),
        struct .pack ('<q',self .offset ),
        struct .pack ('<i',self .limit ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _precise =bool (flags &1 )
        _cdn_supported =bool (flags &2 )
        _location =reader .tgread_object ()
        _offset =reader .read_long ()
        _limit =reader .read_int ()
        return cls (location =_location ,offset =_offset ,limit =_limit ,precise =_precise ,cdn_supported =_cdn_supported )

class GetFileHashesRequest (TLRequest ):
    CONSTRUCTOR_ID =0x9156982a 
    SUBCLASS_OF_ID =0xa5940726 

    def __init__ (self ,location :'TypeInputFileLocation',offset :int ):
        """"""
        self .location =location 
        self .offset =offset 

    def to_dict (self ):
        return {
        '_':'GetFileHashesRequest',
        'location':self .location .to_dict ()if isinstance (self .location ,TLObject )else self .location ,
        'offset':self .offset 
        }

    def _bytes (self ):
        return b''.join ((
        b'*\x98V\x91',
        self .location ._bytes (),
        struct .pack ('<q',self .offset ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _location =reader .tgread_object ()
        _offset =reader .read_long ()
        return cls (location =_location ,offset =_offset )

class GetWebFileRequest (TLRequest ):
    CONSTRUCTOR_ID =0x24e6818d 
    SUBCLASS_OF_ID =0x68f17f51 

    def __init__ (self ,location :'TypeInputWebFileLocation',offset :int ,limit :int ):
        """"""
        self .location =location 
        self .offset =offset 
        self .limit =limit 

    def to_dict (self ):
        return {
        '_':'GetWebFileRequest',
        'location':self .location .to_dict ()if isinstance (self .location ,TLObject )else self .location ,
        'offset':self .offset ,
        'limit':self .limit 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x8d\x81\xe6$',
        self .location ._bytes (),
        struct .pack ('<i',self .offset ),
        struct .pack ('<i',self .limit ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _location =reader .tgread_object ()
        _offset =reader .read_int ()
        _limit =reader .read_int ()
        return cls (location =_location ,offset =_offset ,limit =_limit )

class ReuploadCdnFileRequest (TLRequest ):
    CONSTRUCTOR_ID =0x9b2754a8 
    SUBCLASS_OF_ID =0xa5940726 

    def __init__ (self ,file_token :bytes ,request_token :bytes ):
        """"""
        self .file_token =file_token 
        self .request_token =request_token 

    def to_dict (self ):
        return {
        '_':'ReuploadCdnFileRequest',
        'file_token':self .file_token ,
        'request_token':self .request_token 
        }

    def _bytes (self ):
        return b''.join ((
        b"\xa8T'\x9b",
        self .serialize_bytes (self .file_token ),
        self .serialize_bytes (self .request_token ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _file_token =reader .tgread_bytes ()
        _request_token =reader .tgread_bytes ()
        return cls (file_token =_file_token ,request_token =_request_token )

class SaveBigFilePartRequest (TLRequest ):
    CONSTRUCTOR_ID =0xde7b673d 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,file_id :int ,file_part :int ,file_total_parts :int ,bytes :bytes ):
        """"""
        self .file_id =file_id 
        self .file_part =file_part 
        self .file_total_parts =file_total_parts 
        self .bytes =bytes 

    def to_dict (self ):
        return {
        '_':'SaveBigFilePartRequest',
        'file_id':self .file_id ,
        'file_part':self .file_part ,
        'file_total_parts':self .file_total_parts ,
        'bytes':self .bytes 
        }

    def _bytes (self ):
        return b''.join ((
        b'=g{\xde',
        struct .pack ('<q',self .file_id ),
        struct .pack ('<i',self .file_part ),
        struct .pack ('<i',self .file_total_parts ),
        self .serialize_bytes (self .bytes ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _file_id =reader .read_long ()
        _file_part =reader .read_int ()
        _file_total_parts =reader .read_int ()
        _bytes =reader .tgread_bytes ()
        return cls (file_id =_file_id ,file_part =_file_part ,file_total_parts =_file_total_parts ,bytes =_bytes )

class SaveFilePartRequest (TLRequest ):
    CONSTRUCTOR_ID =0xb304a621 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,file_id :int ,file_part :int ,bytes :bytes ):
        """"""
        self .file_id =file_id 
        self .file_part =file_part 
        self .bytes =bytes 

    def to_dict (self ):
        return {
        '_':'SaveFilePartRequest',
        'file_id':self .file_id ,
        'file_part':self .file_part ,
        'bytes':self .bytes 
        }

    def _bytes (self ):
        return b''.join ((
        b'!\xa6\x04\xb3',
        struct .pack ('<q',self .file_id ),
        struct .pack ('<i',self .file_part ),
        self .serialize_bytes (self .bytes ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _file_id =reader .read_long ()
        _file_part =reader .read_int ()
        _bytes =reader .tgread_bytes ()
        return cls (file_id =_file_id ,file_part =_file_part ,bytes =_bytes )

