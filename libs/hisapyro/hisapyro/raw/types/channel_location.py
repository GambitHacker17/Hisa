
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelLocation (TLObject ):
    """"""

    __slots__ :List [str ]=["geo_point","address"]

    ID =0x209b82db 
    QUALNAME ="types.ChannelLocation"

    def __init__ (self ,*,geo_point :"raw.base.GeoPoint",address :str )->None :
        self .geo_point =geo_point 
        self .address =address 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelLocation":

        geo_point =TLObject .read (b )

        address =String .read (b )

        return ChannelLocation (geo_point =geo_point ,address =address )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .geo_point .write ())

        b .write (String (self .address ))

        return b .getvalue ()
