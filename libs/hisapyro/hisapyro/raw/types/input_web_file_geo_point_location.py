
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputWebFileGeoPointLocation (TLObject ):
    """"""

    __slots__ :List [str ]=["geo_point","access_hash","w","h","zoom","scale"]

    ID =0x9f2221c9 
    QUALNAME ="types.InputWebFileGeoPointLocation"

    def __init__ (self ,*,geo_point :"raw.base.InputGeoPoint",access_hash :int ,w :int ,h :int ,zoom :int ,scale :int )->None :
        self .geo_point =geo_point 
        self .access_hash =access_hash 
        self .w =w 
        self .h =h 
        self .zoom =zoom 
        self .scale =scale 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputWebFileGeoPointLocation":

        geo_point =TLObject .read (b )

        access_hash =Long .read (b )

        w =Int .read (b )

        h =Int .read (b )

        zoom =Int .read (b )

        scale =Int .read (b )

        return InputWebFileGeoPointLocation (geo_point =geo_point ,access_hash =access_hash ,w =w ,h =h ,zoom =zoom ,scale =scale )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .geo_point .write ())

        b .write (Long (self .access_hash ))

        b .write (Int (self .w ))

        b .write (Int (self .h ))

        b .write (Int (self .zoom ))

        b .write (Int (self .scale ))

        return b .getvalue ()
