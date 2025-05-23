""""""
from ...tl .tlobject import TLObject 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 

class FileGif (TLObject ):
    CONSTRUCTOR_ID =0xcae1aadf 
    SUBCLASS_OF_ID =0xf3a1e6f3 

    def to_dict (self ):
        return {
        '_':'FileGif'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xdf\xaa\xe1\xca',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class FileJpeg (TLObject ):
    CONSTRUCTOR_ID =0x7efe0e 
    SUBCLASS_OF_ID =0xf3a1e6f3 

    def to_dict (self ):
        return {
        '_':'FileJpeg'
        }

    def _bytes (self ):
        return b''.join ((
        b'\x0e\xfe~\x00',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class FileMov (TLObject ):
    CONSTRUCTOR_ID =0x4b09ebbc 
    SUBCLASS_OF_ID =0xf3a1e6f3 

    def to_dict (self ):
        return {
        '_':'FileMov'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xbc\xeb\tK',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class FileMp3 (TLObject ):
    CONSTRUCTOR_ID =0x528a0677 
    SUBCLASS_OF_ID =0xf3a1e6f3 

    def to_dict (self ):
        return {
        '_':'FileMp3'
        }

    def _bytes (self ):
        return b''.join ((
        b'w\x06\x8aR',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class FileMp4 (TLObject ):
    CONSTRUCTOR_ID =0xb3cea0e4 
    SUBCLASS_OF_ID =0xf3a1e6f3 

    def to_dict (self ):
        return {
        '_':'FileMp4'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xe4\xa0\xce\xb3',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class FilePartial (TLObject ):
    CONSTRUCTOR_ID =0x40bc6f52 
    SUBCLASS_OF_ID =0xf3a1e6f3 

    def to_dict (self ):
        return {
        '_':'FilePartial'
        }

    def _bytes (self ):
        return b''.join ((
        b'Ro\xbc@',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class FilePdf (TLObject ):
    CONSTRUCTOR_ID =0xae1e508d 
    SUBCLASS_OF_ID =0xf3a1e6f3 

    def to_dict (self ):
        return {
        '_':'FilePdf'
        }

    def _bytes (self ):
        return b''.join ((
        b'\x8dP\x1e\xae',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class FilePng (TLObject ):
    CONSTRUCTOR_ID =0xa4f63c0 
    SUBCLASS_OF_ID =0xf3a1e6f3 

    def to_dict (self ):
        return {
        '_':'FilePng'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc0cO\n',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class FileUnknown (TLObject ):
    CONSTRUCTOR_ID =0xaa963b05 
    SUBCLASS_OF_ID =0xf3a1e6f3 

    def to_dict (self ):
        return {
        '_':'FileUnknown'
        }

    def _bytes (self ):
        return b''.join ((
        b'\x05;\x96\xaa',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class FileWebp (TLObject ):
    CONSTRUCTOR_ID =0x1081464c 
    SUBCLASS_OF_ID =0xf3a1e6f3 

    def to_dict (self ):
        return {
        '_':'FileWebp'
        }

    def _bytes (self ):
        return b''.join ((
        b'LF\x81\x10',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

