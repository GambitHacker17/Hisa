
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class CountriesList (TLObject ):
    """"""

    __slots__ :List [str ]=["countries","hash"]

    ID =0x87d0759e 
    QUALNAME ="types.help.CountriesList"

    def __init__ (self ,*,countries :List ["raw.base.help.Country"],hash :int )->None :
        self .countries =countries 
        self .hash =hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"CountriesList":

        countries =TLObject .read (b )

        hash =Int .read (b )

        return CountriesList (countries =countries ,hash =hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .countries ))

        b .write (Int (self .hash ))

        return b .getvalue ()
