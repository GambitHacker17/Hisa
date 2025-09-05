
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PageBlockPullquote (TLObject ):
    """"""

    __slots__ :List [str ]=["text","caption"]

    ID =0x4f4456d3 
    QUALNAME ="types.PageBlockPullquote"

    def __init__ (self ,*,text :"raw.base.RichText",caption :"raw.base.RichText")->None :
        self .text =text 
        self .caption =caption 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PageBlockPullquote":

        text =TLObject .read (b )

        caption =TLObject .read (b )

        return PageBlockPullquote (text =text ,caption =caption )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .text .write ())

        b .write (self .caption .write ())

        return b .getvalue ()
