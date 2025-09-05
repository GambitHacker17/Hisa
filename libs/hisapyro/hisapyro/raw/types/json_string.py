
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class JsonString (TLObject ):
    """"""

    __slots__ :List [str ]=["value"]

    ID =0xb71e767a 
    QUALNAME ="types.JsonString"

    def __init__ (self ,*,value :str )->None :
        self .value =value 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"JsonString":

        value =String .read (b )

        return JsonString (value =value )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .value ))

        return b .getvalue ()
