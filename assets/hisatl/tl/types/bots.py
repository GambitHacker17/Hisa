""""""
from ...tl .tlobject import TLObject 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 

class BotInfo (TLObject ):
    CONSTRUCTOR_ID =0xe8a775b0 
    SUBCLASS_OF_ID =0xca7b2235 

    def __init__ (self ,name :str ,about :str ,description :str ):
        """"""
        self .name =name 
        self .about =about 
        self .description =description 

    def to_dict (self ):
        return {
        '_':'BotInfo',
        'name':self .name ,
        'about':self .about ,
        'description':self .description 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xb0u\xa7\xe8',
        self .serialize_bytes (self .name ),
        self .serialize_bytes (self .about ),
        self .serialize_bytes (self .description ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _name =reader .tgread_string ()
        _about =reader .tgread_string ()
        _description =reader .tgread_string ()
        return cls (name =_name ,about =_about ,description =_description )

