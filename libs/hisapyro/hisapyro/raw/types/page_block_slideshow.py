
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PageBlockSlideshow (TLObject ):
    """"""

    __slots__ :List [str ]=["items","caption"]

    ID =0x31f9590 
    QUALNAME ="types.PageBlockSlideshow"

    def __init__ (self ,*,items :List ["raw.base.PageBlock"],caption :"raw.base.PageCaption")->None :
        self .items =items 
        self .caption =caption 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PageBlockSlideshow":

        items =TLObject .read (b )

        caption =TLObject .read (b )

        return PageBlockSlideshow (items =items ,caption =caption )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .items ))

        b .write (self .caption .write ())

        return b .getvalue ()
