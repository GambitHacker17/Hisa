
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PageBlockPreformatted (TLObject ):
    """"""

    __slots__ :List [str ]=["text","language"]

    ID =0xc070d93e 
    QUALNAME ="types.PageBlockPreformatted"

    def __init__ (self ,*,text :"raw.base.RichText",language :str )->None :
        self .text =text 
        self .language =language 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PageBlockPreformatted":

        text =TLObject .read (b )

        language =String .read (b )

        return PageBlockPreformatted (text =text ,language =language )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .text .write ())

        b .write (String (self .language ))

        return b .getvalue ()
