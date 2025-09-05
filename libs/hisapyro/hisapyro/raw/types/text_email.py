
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class TextEmail (TLObject ):
    """"""

    __slots__ :List [str ]=["text","email"]

    ID =0xde5a0dd6 
    QUALNAME ="types.TextEmail"

    def __init__ (self ,*,text :"raw.base.RichText",email :str )->None :
        self .text =text 
        self .email =email 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"TextEmail":

        text =TLObject .read (b )

        email =String .read (b )

        return TextEmail (text =text ,email =email )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .text .write ())

        b .write (String (self .email ))

        return b .getvalue ()
