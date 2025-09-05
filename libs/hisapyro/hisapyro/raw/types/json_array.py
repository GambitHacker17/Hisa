
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class JsonArray (TLObject ):
    """"""

    __slots__ :List [str ]=["value"]

    ID =0xf7444763 
    QUALNAME ="types.JsonArray"

    def __init__ (self ,*,value :List ["raw.base.JSONValue"])->None :
        self .value =value 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"JsonArray":

        value =TLObject .read (b )

        return JsonArray (value =value )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .value ))

        return b .getvalue ()
