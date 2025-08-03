
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GroupCallStreamChannel (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","scale","last_timestamp_ms"]

    ID =0x80eb48af 
    QUALNAME ="types.GroupCallStreamChannel"

    def __init__ (self ,*,channel :int ,scale :int ,last_timestamp_ms :int )->None :
        self .channel =channel 
        self .scale =scale 
        self .last_timestamp_ms =last_timestamp_ms 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GroupCallStreamChannel":

        channel =Int .read (b )

        scale =Int .read (b )

        last_timestamp_ms =Long .read (b )

        return GroupCallStreamChannel (channel =channel ,scale =scale ,last_timestamp_ms =last_timestamp_ms )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .channel ))

        b .write (Int (self .scale ))

        b .write (Long (self .last_timestamp_ms ))

        return b .getvalue ()
