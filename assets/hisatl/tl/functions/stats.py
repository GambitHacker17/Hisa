""""""
from ...tl .tlobject import TLObject 
from ...tl .tlobject import TLRequest 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeInputChannel ,TypeInputPeer 

class GetBroadcastStatsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xab42441a 
    SUBCLASS_OF_ID =0x7ff25428 

    def __init__ (self ,channel :'TypeInputChannel',dark :Optional [bool ]=None ):
        """"""
        self .channel =channel 
        self .dark =dark 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'GetBroadcastStatsRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'dark':self .dark 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x1aDB\xab',
        struct .pack ('<I',(0 if self .dark is None or self .dark is False else 1 )),
        self .channel ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _dark =bool (flags &1 )
        _channel =reader .tgread_object ()
        return cls (channel =_channel ,dark =_dark )

class GetMegagroupStatsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xdcdf8607 
    SUBCLASS_OF_ID =0x5b59be8d 

    def __init__ (self ,channel :'TypeInputChannel',dark :Optional [bool ]=None ):
        """"""
        self .channel =channel 
        self .dark =dark 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'GetMegagroupStatsRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'dark':self .dark 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x07\x86\xdf\xdc',
        struct .pack ('<I',(0 if self .dark is None or self .dark is False else 1 )),
        self .channel ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _dark =bool (flags &1 )
        _channel =reader .tgread_object ()
        return cls (channel =_channel ,dark =_dark )

class GetMessagePublicForwardsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x5630281b 
    SUBCLASS_OF_ID =0xd4b40b5e 

    def __init__ (self ,channel :'TypeInputChannel',msg_id :int ,offset_rate :int ,offset_peer :'TypeInputPeer',offset_id :int ,limit :int ):
        """"""
        self .channel =channel 
        self .msg_id =msg_id 
        self .offset_rate =offset_rate 
        self .offset_peer =offset_peer 
        self .offset_id =offset_id 
        self .limit =limit 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))
        self .offset_peer =utils .get_input_peer (await client .get_input_entity (self .offset_peer ))

    def to_dict (self ):
        return {
        '_':'GetMessagePublicForwardsRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'msg_id':self .msg_id ,
        'offset_rate':self .offset_rate ,
        'offset_peer':self .offset_peer .to_dict ()if isinstance (self .offset_peer ,TLObject )else self .offset_peer ,
        'offset_id':self .offset_id ,
        'limit':self .limit 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x1b(0V',
        self .channel ._bytes (),
        struct .pack ('<i',self .msg_id ),
        struct .pack ('<i',self .offset_rate ),
        self .offset_peer ._bytes (),
        struct .pack ('<i',self .offset_id ),
        struct .pack ('<i',self .limit ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _msg_id =reader .read_int ()
        _offset_rate =reader .read_int ()
        _offset_peer =reader .tgread_object ()
        _offset_id =reader .read_int ()
        _limit =reader .read_int ()
        return cls (channel =_channel ,msg_id =_msg_id ,offset_rate =_offset_rate ,offset_peer =_offset_peer ,offset_id =_offset_id ,limit =_limit )

class GetMessageStatsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xb6e0a3f5 
    SUBCLASS_OF_ID =0x9604a322 

    def __init__ (self ,channel :'TypeInputChannel',msg_id :int ,dark :Optional [bool ]=None ):
        """"""
        self .channel =channel 
        self .msg_id =msg_id 
        self .dark =dark 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'GetMessageStatsRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'msg_id':self .msg_id ,
        'dark':self .dark 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf5\xa3\xe0\xb6',
        struct .pack ('<I',(0 if self .dark is None or self .dark is False else 1 )),
        self .channel ._bytes (),
        struct .pack ('<i',self .msg_id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _dark =bool (flags &1 )
        _channel =reader .tgread_object ()
        _msg_id =reader .read_int ()
        return cls (channel =_channel ,msg_id =_msg_id ,dark =_dark )

class LoadAsyncGraphRequest (TLRequest ):
    CONSTRUCTOR_ID =0x621d5fa0 
    SUBCLASS_OF_ID =0x9b903153 

    def __init__ (self ,token :str ,x :Optional [int ]=None ):
        """"""
        self .token =token 
        self .x =x 

    def to_dict (self ):
        return {
        '_':'LoadAsyncGraphRequest',
        'token':self .token ,
        'x':self .x 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xa0_\x1db',
        struct .pack ('<I',(0 if self .x is None or self .x is False else 1 )),
        self .serialize_bytes (self .token ),
        b''if self .x is None or self .x is False else (struct .pack ('<q',self .x )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _token =reader .tgread_string ()
        if flags &1 :
            _x =reader .read_long ()
        else :
            _x =None 
        return cls (token =_token ,x =_x )

