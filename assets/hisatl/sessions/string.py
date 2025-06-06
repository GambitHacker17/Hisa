import base64 
import ipaddress 
import struct 

from .abstract import Session 
from .memory import MemorySession 
from ..crypto import AuthKey 

_STRUCT_PREFORMAT ='>B{}sH256s'

CURRENT_VERSION ='1'

class StringSession (MemorySession ):
    """"""
    def __init__ (self ,string :str =None ):
        super ().__init__ ()
        if string :
            if string [0 ]!=CURRENT_VERSION :
                raise ValueError ('Not a valid string')

            string =string [1 :]
            ip_len =4 if len (string )==352 else 16 
            self ._dc_id ,ip ,self ._port ,key =struct .unpack (
            _STRUCT_PREFORMAT .format (ip_len ),StringSession .decode (string ))

            self ._server_address =ipaddress .ip_address (ip ).compressed 
            if any (key ):
                self ._auth_key =AuthKey (key )

    @staticmethod 
    def encode (x :bytes )->str :
        return base64 .urlsafe_b64encode (x ).decode ('ascii')

    @staticmethod 
    def decode (x :str )->bytes :
        return base64 .urlsafe_b64decode (x )

    def save (self :Session ):
        if not self .auth_key :
            return ''

        ip =ipaddress .ip_address (self .server_address ).packed 
        return CURRENT_VERSION +StringSession .encode (struct .pack (
        _STRUCT_PREFORMAT .format (len (ip )),
        self .dc_id ,
        ip ,
        self .port ,
        self .auth_key .key 
        ))
