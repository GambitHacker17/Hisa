
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PageBlockAnchor (TLObject ):
    """"""

    __slots__ :List [str ]=["name"]

    ID =0xce0d37b0 
    QUALNAME ="types.PageBlockAnchor"

    def __init__ (self ,*,name :str )->None :
        self .name =name 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PageBlockAnchor":

        name =String .read (b )

        return PageBlockAnchor (name =name )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .name ))

        return b .getvalue ()
