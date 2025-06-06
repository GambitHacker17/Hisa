""""""
from ...tl .tlobject import TLObject 
from ...tl .tlobject import TLRequest 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeChannelMessagesFilter ,TypeInputChannel 

class GetChannelDifferenceRequest (TLRequest ):
    CONSTRUCTOR_ID =0x3173d78 
    SUBCLASS_OF_ID =0x29896f5d 

    def __init__ (self ,channel :'TypeInputChannel',filter :'TypeChannelMessagesFilter',pts :int ,limit :int ,force :Optional [bool ]=None ):
        """"""
        self .channel =channel 
        self .filter =filter 
        self .pts =pts 
        self .limit =limit 
        self .force =force 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'GetChannelDifferenceRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'filter':self .filter .to_dict ()if isinstance (self .filter ,TLObject )else self .filter ,
        'pts':self .pts ,
        'limit':self .limit ,
        'force':self .force 
        }

    def _bytes (self ):
        return b''.join ((
        b'x=\x17\x03',
        struct .pack ('<I',(0 if self .force is None or self .force is False else 1 )),
        self .channel ._bytes (),
        self .filter ._bytes (),
        struct .pack ('<i',self .pts ),
        struct .pack ('<i',self .limit ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _force =bool (flags &1 )
        _channel =reader .tgread_object ()
        _filter =reader .tgread_object ()
        _pts =reader .read_int ()
        _limit =reader .read_int ()
        return cls (channel =_channel ,filter =_filter ,pts =_pts ,limit =_limit ,force =_force )

class GetDifferenceRequest (TLRequest ):
    CONSTRUCTOR_ID =0x19c2f763 
    SUBCLASS_OF_ID =0x20482874 

    def __init__ (self ,pts :int ,date :Optional [datetime ],qts :int ,pts_limit :Optional [int ]=None ,pts_total_limit :Optional [int ]=None ,qts_limit :Optional [int ]=None ):
        """"""
        self .pts =pts 
        self .date =date 
        self .qts =qts 
        self .pts_limit =pts_limit 
        self .pts_total_limit =pts_total_limit 
        self .qts_limit =qts_limit 

    def to_dict (self ):
        return {
        '_':'GetDifferenceRequest',
        'pts':self .pts ,
        'date':self .date ,
        'qts':self .qts ,
        'pts_limit':self .pts_limit ,
        'pts_total_limit':self .pts_total_limit ,
        'qts_limit':self .qts_limit 
        }

    def _bytes (self ):
        return b''.join ((
        b'c\xf7\xc2\x19',
        struct .pack ('<I',(0 if self .pts_limit is None or self .pts_limit is False else 2 )|(0 if self .pts_total_limit is None or self .pts_total_limit is False else 1 )|(0 if self .qts_limit is None or self .qts_limit is False else 4 )),
        struct .pack ('<i',self .pts ),
        b''if self .pts_limit is None or self .pts_limit is False else (struct .pack ('<i',self .pts_limit )),
        b''if self .pts_total_limit is None or self .pts_total_limit is False else (struct .pack ('<i',self .pts_total_limit )),
        self .serialize_datetime (self .date ),
        struct .pack ('<i',self .qts ),
        b''if self .qts_limit is None or self .qts_limit is False else (struct .pack ('<i',self .qts_limit )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _pts =reader .read_int ()
        if flags &2 :
            _pts_limit =reader .read_int ()
        else :
            _pts_limit =None 
        if flags &1 :
            _pts_total_limit =reader .read_int ()
        else :
            _pts_total_limit =None 
        _date =reader .tgread_date ()
        _qts =reader .read_int ()
        if flags &4 :
            _qts_limit =reader .read_int ()
        else :
            _qts_limit =None 
        return cls (pts =_pts ,date =_date ,qts =_qts ,pts_limit =_pts_limit ,pts_total_limit =_pts_total_limit ,qts_limit =_qts_limit )

class GetStateRequest (TLRequest ):
    CONSTRUCTOR_ID =0xedd4882a 
    SUBCLASS_OF_ID =0x23df1a01 

    def to_dict (self ):
        return {
        '_':'GetStateRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'*\x88\xd4\xed',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

