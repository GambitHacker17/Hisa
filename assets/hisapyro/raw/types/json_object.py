
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class JsonObject (TLObject ):
    """"""

    __slots__ :List [str ]=["value"]

    ID =0x99c1d49d 
    QUALNAME ="types.JsonObject"

    def __init__ (self ,*,value :List ["raw.base.JSONObjectValue"])->None :
        self .value =value 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"JsonObject":

        value =TLObject .read (b )

        return JsonObject (value =value )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .value ))

        return b .getvalue ()
