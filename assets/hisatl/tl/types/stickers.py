""""""
from ...tl .tlobject import TLObject 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 

class SuggestedShortName (TLObject ):
    CONSTRUCTOR_ID =0x85fea03f 
    SUBCLASS_OF_ID =0xc44a4b21 

    def __init__ (self ,short_name :str ):
        """"""
        self .short_name =short_name 

    def to_dict (self ):
        return {
        '_':'SuggestedShortName',
        'short_name':self .short_name 
        }

    def _bytes (self ):
        return b''.join ((
        b'?\xa0\xfe\x85',
        self .serialize_bytes (self .short_name ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _short_name =reader .tgread_string ()
        return cls (short_name =_short_name )

