
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class LangPackStringDeleted (TLObject ):
    """"""

    __slots__ :List [str ]=["key"]

    ID =0x2979eeb2 
    QUALNAME ="types.LangPackStringDeleted"

    def __init__ (self ,*,key :str )->None :
        self .key =key 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"LangPackStringDeleted":

        key =String .read (b )

        return LangPackStringDeleted (key =key )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .key ))

        return b .getvalue ()
