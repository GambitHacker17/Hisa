
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PageListOrderedItemBlocks (TLObject ):
    """"""

    __slots__ :List [str ]=["num","blocks"]

    ID =0x98dd8936 
    QUALNAME ="types.PageListOrderedItemBlocks"

    def __init__ (self ,*,num :str ,blocks :List ["raw.base.PageBlock"])->None :
        self .num =num 
        self .blocks =blocks 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PageListOrderedItemBlocks":

        num =String .read (b )

        blocks =TLObject .read (b )

        return PageListOrderedItemBlocks (num =num ,blocks =blocks )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .num ))

        b .write (Vector (self .blocks ))

        return b .getvalue ()
