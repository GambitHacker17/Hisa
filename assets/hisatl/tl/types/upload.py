""""""
from ...tl .tlobject import TLObject 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types .storage import TypeFileType 
    from ...tl .types import TypeFileHash 

class CdnFile (TLObject ):
    CONSTRUCTOR_ID =0xa99fca4f 
    SUBCLASS_OF_ID =0xf5ccf928 

    def __init__ (self ,bytes :bytes ):
        """"""
        self .bytes =bytes 

    def to_dict (self ):
        return {
        '_':'CdnFile',
        'bytes':self .bytes 
        }

    def _bytes (self ):
        return b''.join ((
        b'O\xca\x9f\xa9',
        self .serialize_bytes (self .bytes ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _bytes =reader .tgread_bytes ()
        return cls (bytes =_bytes )

class CdnFileReuploadNeeded (TLObject ):
    CONSTRUCTOR_ID =0xeea8e46e 
    SUBCLASS_OF_ID =0xf5ccf928 

    def __init__ (self ,request_token :bytes ):
        """"""
        self .request_token =request_token 

    def to_dict (self ):
        return {
        '_':'CdnFileReuploadNeeded',
        'request_token':self .request_token 
        }

    def _bytes (self ):
        return b''.join ((
        b'n\xe4\xa8\xee',
        self .serialize_bytes (self .request_token ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _request_token =reader .tgread_bytes ()
        return cls (request_token =_request_token )

class File (TLObject ):
    CONSTRUCTOR_ID =0x96a18d5 
    SUBCLASS_OF_ID =0x6c9bd728 

    def __init__ (self ,type :'TypeFileType',mtime :int ,bytes :bytes ):
        """"""
        self .type =type 
        self .mtime =mtime 
        self .bytes =bytes 

    def to_dict (self ):
        return {
        '_':'File',
        'type':self .type .to_dict ()if isinstance (self .type ,TLObject )else self .type ,
        'mtime':self .mtime ,
        'bytes':self .bytes 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xd5\x18j\t',
        self .type ._bytes (),
        struct .pack ('<i',self .mtime ),
        self .serialize_bytes (self .bytes ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _type =reader .tgread_object ()
        _mtime =reader .read_int ()
        _bytes =reader .tgread_bytes ()
        return cls (type =_type ,mtime =_mtime ,bytes =_bytes )

class FileCdnRedirect (TLObject ):
    CONSTRUCTOR_ID =0xf18cda44 
    SUBCLASS_OF_ID =0x6c9bd728 

    def __init__ (self ,dc_id :int ,file_token :bytes ,encryption_key :bytes ,encryption_iv :bytes ,file_hashes :List ['TypeFileHash']):
        """"""
        self .dc_id =dc_id 
        self .file_token =file_token 
        self .encryption_key =encryption_key 
        self .encryption_iv =encryption_iv 
        self .file_hashes =file_hashes 

    def to_dict (self ):
        return {
        '_':'FileCdnRedirect',
        'dc_id':self .dc_id ,
        'file_token':self .file_token ,
        'encryption_key':self .encryption_key ,
        'encryption_iv':self .encryption_iv ,
        'file_hashes':[]if self .file_hashes is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .file_hashes ]
        }

    def _bytes (self ):
        return b''.join ((
        b'D\xda\x8c\xf1',
        struct .pack ('<i',self .dc_id ),
        self .serialize_bytes (self .file_token ),
        self .serialize_bytes (self .encryption_key ),
        self .serialize_bytes (self .encryption_iv ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .file_hashes )),b''.join (x ._bytes ()for x in self .file_hashes ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _dc_id =reader .read_int ()
        _file_token =reader .tgread_bytes ()
        _encryption_key =reader .tgread_bytes ()
        _encryption_iv =reader .tgread_bytes ()
        reader .read_int ()
        _file_hashes =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _file_hashes .append (_x )

        return cls (dc_id =_dc_id ,file_token =_file_token ,encryption_key =_encryption_key ,encryption_iv =_encryption_iv ,file_hashes =_file_hashes )

class WebFile (TLObject ):
    CONSTRUCTOR_ID =0x21e753bc 
    SUBCLASS_OF_ID =0x68f17f51 

    def __init__ (self ,size :int ,mime_type :str ,file_type :'TypeFileType',mtime :int ,bytes :bytes ):
        """"""
        self .size =size 
        self .mime_type =mime_type 
        self .file_type =file_type 
        self .mtime =mtime 
        self .bytes =bytes 

    def to_dict (self ):
        return {
        '_':'WebFile',
        'size':self .size ,
        'mime_type':self .mime_type ,
        'file_type':self .file_type .to_dict ()if isinstance (self .file_type ,TLObject )else self .file_type ,
        'mtime':self .mtime ,
        'bytes':self .bytes 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xbcS\xe7!',
        struct .pack ('<i',self .size ),
        self .serialize_bytes (self .mime_type ),
        self .file_type ._bytes (),
        struct .pack ('<i',self .mtime ),
        self .serialize_bytes (self .bytes ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _size =reader .read_int ()
        _mime_type =reader .tgread_string ()
        _file_type =reader .tgread_object ()
        _mtime =reader .read_int ()
        _bytes =reader .tgread_bytes ()
        return cls (size =_size ,mime_type =_mime_type ,file_type =_file_type ,mtime =_mtime ,bytes =_bytes )

