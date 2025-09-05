
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class NearestDc (TLObject ):
    """"""

    __slots__ :List [str ]=["country","this_dc","nearest_dc"]

    ID =0x8e1a1775 
    QUALNAME ="types.NearestDc"

    def __init__ (self ,*,country :str ,this_dc :int ,nearest_dc :int )->None :
        self .country =country 
        self .this_dc =this_dc 
        self .nearest_dc =nearest_dc 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"NearestDc":

        country =String .read (b )

        this_dc =Int .read (b )

        nearest_dc =Int .read (b )

        return NearestDc (country =country ,this_dc =this_dc ,nearest_dc =nearest_dc )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .country ))

        b .write (Int (self .this_dc ))

        b .write (Int (self .nearest_dc ))

        return b .getvalue ()
