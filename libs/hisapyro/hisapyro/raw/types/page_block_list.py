
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PageBlockList (TLObject ):
    """"""

    __slots__ :List [str ]=["items"]

    ID =0xe4e88011 
    QUALNAME ="types.PageBlockList"

    def __init__ (self ,*,items :List ["raw.base.PageListItem"])->None :
        self .items =items 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PageBlockList":

        items =TLObject .read (b )

        return PageBlockList (items =items )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .items ))

        return b .getvalue ()
