""""""
from ...tl .tlobject import TLObject 
from ...tl .tlobject import TLRequest 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeInputPeer 

class ApplyBoostRequest (TLRequest ):
    CONSTRUCTOR_ID =0x6b7da746 
    SUBCLASS_OF_ID =0xad3512db 

    def __init__ (self ,peer :'TypeInputPeer',slots :Optional [List [int ]]=None ):
        """"""
        self .peer =peer 
        self .slots =slots 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'ApplyBoostRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'slots':[]if self .slots is None else self .slots [:]
        }

    def _bytes (self ):
        return b''.join ((
        b'F\xa7}k',
        struct .pack ('<I',(0 if self .slots is None or self .slots is False else 1 )),
        b''if self .slots is None or self .slots is False else b''.join ((b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .slots )),b''.join (struct .pack ('<i',x )for x in self .slots ))),
        self .peer ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        if flags &1 :
            reader .read_int ()
            _slots =[]
            for _ in range (reader .read_int ()):
                _x =reader .read_int ()
                _slots .append (_x )

        else :
            _slots =None 
        _peer =reader .tgread_object ()
        return cls (peer =_peer ,slots =_slots )

class GetBoostsListRequest (TLRequest ):
    CONSTRUCTOR_ID =0x60f67660 
    SUBCLASS_OF_ID =0x2235a8bd 

    def __init__ (self ,peer :'TypeInputPeer',offset :str ,limit :int ,gifts :Optional [bool ]=None ):
        """"""
        self .peer =peer 
        self .offset =offset 
        self .limit =limit 
        self .gifts =gifts 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'GetBoostsListRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'offset':self .offset ,
        'limit':self .limit ,
        'gifts':self .gifts 
        }

    def _bytes (self ):
        return b''.join ((
        b'`v\xf6`',
        struct .pack ('<I',(0 if self .gifts is None or self .gifts is False else 1 )),
        self .peer ._bytes (),
        self .serialize_bytes (self .offset ),
        struct .pack ('<i',self .limit ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _gifts =bool (flags &1 )
        _peer =reader .tgread_object ()
        _offset =reader .tgread_string ()
        _limit =reader .read_int ()
        return cls (peer =_peer ,offset =_offset ,limit =_limit ,gifts =_gifts )

class GetBoostsStatusRequest (TLRequest ):
    CONSTRUCTOR_ID =0x42f1f61 
    SUBCLASS_OF_ID =0xc31b1ab9 

    def __init__ (self ,peer :'TypeInputPeer'):
        """"""
        self .peer =peer 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'GetBoostsStatusRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer 
        }

    def _bytes (self ):
        return b''.join ((
        b'a\x1f/\x04',
        self .peer ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        return cls (peer =_peer )

class GetMyBoostsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xbe77b4a 
    SUBCLASS_OF_ID =0xad3512db 

    def to_dict (self ):
        return {
        '_':'GetMyBoostsRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'J{\xe7\x0b',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

