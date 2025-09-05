
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PageListOrderedItemText (TLObject ):
    """"""

    __slots__ :List [str ]=["num","text"]

    ID =0x5e068047 
    QUALNAME ="types.PageListOrderedItemText"

    def __init__ (self ,*,num :str ,text :"raw.base.RichText")->None :
        self .num =num 
        self .text =text 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PageListOrderedItemText":

        num =String .read (b )

        text =TLObject .read (b )

        return PageListOrderedItemText (num =num ,text =text )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .num ))

        b .write (self .text .write ())

        return b .getvalue ()
