
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class TextFixed (TLObject ):
    """"""

    __slots__ :List [str ]=["text"]

    ID =0x6c3f19b9 
    QUALNAME ="types.TextFixed"

    def __init__ (self ,*,text :"raw.base.RichText")->None :
        self .text =text 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"TextFixed":

        text =TLObject .read (b )

        return TextFixed (text =text )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .text .write ())

        return b .getvalue ()
