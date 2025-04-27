
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class JsonObjectValue (TLObject ):
    """"""

    __slots__ :List [str ]=["key","value"]

    ID =0xc0de1bd9 
    QUALNAME ="types.JsonObjectValue"

    def __init__ (self ,*,key :str ,value :"raw.base.JSONValue")->None :
        self .key =key 
        self .value =value 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"JsonObjectValue":

        key =String .read (b )

        value =TLObject .read (b )

        return JsonObjectValue (key =key ,value =value )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .key ))

        b .write (self .value .write ())

        return b .getvalue ()
