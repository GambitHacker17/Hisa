
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class JsonBool (TLObject ):
    """"""

    __slots__ :List [str ]=["value"]

    ID =0xc7345e6a 
    QUALNAME ="types.JsonBool"

    def __init__ (self ,*,value :bool )->None :
        self .value =value 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"JsonBool":

        value =Bool .read (b )

        return JsonBool (value =value )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Bool (self .value ))

        return b .getvalue ()
