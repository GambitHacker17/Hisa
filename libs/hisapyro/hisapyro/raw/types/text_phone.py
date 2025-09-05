
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class TextPhone (TLObject ):
    """"""

    __slots__ :List [str ]=["text","phone"]

    ID =0x1ccb966a 
    QUALNAME ="types.TextPhone"

    def __init__ (self ,*,text :"raw.base.RichText",phone :str )->None :
        self .text =text 
        self .phone =phone 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"TextPhone":

        text =TLObject .read (b )

        phone =String .read (b )

        return TextPhone (text =text ,phone =phone )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .text .write ())

        b .write (String (self .phone ))

        return b .getvalue ()
