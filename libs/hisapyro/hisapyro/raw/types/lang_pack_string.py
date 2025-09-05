
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class LangPackString (TLObject ):
    """"""

    __slots__ :List [str ]=["key","value"]

    ID =0xcad181f6 
    QUALNAME ="types.LangPackString"

    def __init__ (self ,*,key :str ,value :str )->None :
        self .key =key 
        self .value =value 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"LangPackString":

        key =String .read (b )

        value =String .read (b )

        return LangPackString (key =key ,value =value )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .key ))

        b .write (String (self .value ))

        return b .getvalue ()
