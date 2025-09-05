
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EditLocation (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","geo_point","address"]

    ID =0x58e63f6d 
    QUALNAME ="functions.channels.EditLocation"

    def __init__ (self ,*,channel :"raw.base.InputChannel",geo_point :"raw.base.InputGeoPoint",address :str )->None :
        self .channel =channel 
        self .geo_point =geo_point 
        self .address =address 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EditLocation":

        channel =TLObject .read (b )

        geo_point =TLObject .read (b )

        address =String .read (b )

        return EditLocation (channel =channel ,geo_point =geo_point ,address =address )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .channel .write ())

        b .write (self .geo_point .write ())

        b .write (String (self .address ))

        return b .getvalue ()
