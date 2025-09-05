
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class JsonNumber (TLObject ):
    """"""

    __slots__ :List [str ]=["value"]

    ID =0x2be0dfa4 
    QUALNAME ="types.JsonNumber"

    def __init__ (self ,*,value :float )->None :
        self .value =value 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"JsonNumber":

        value =Double .read (b )

        return JsonNumber (value =value )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Double (self .value ))

        return b .getvalue ()
