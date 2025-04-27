
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SentCodeTypeFlashCall (TLObject ):
    """"""

    __slots__ :List [str ]=["pattern"]

    ID =0xab03c6d9 
    QUALNAME ="types.auth.SentCodeTypeFlashCall"

    def __init__ (self ,*,pattern :str )->None :
        self .pattern =pattern 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SentCodeTypeFlashCall":

        pattern =String .read (b )

        return SentCodeTypeFlashCall (pattern =pattern )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .pattern ))

        return b .getvalue ()
