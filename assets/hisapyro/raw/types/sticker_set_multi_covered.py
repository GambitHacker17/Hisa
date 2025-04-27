
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class StickerSetMultiCovered (TLObject ):
    """"""

    __slots__ :List [str ]=["set","covers"]

    ID =0x3407e51b 
    QUALNAME ="types.StickerSetMultiCovered"

    def __init__ (self ,*,set :"raw.base.StickerSet",covers :List ["raw.base.Document"])->None :
        self .set =set 
        self .covers =covers 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"StickerSetMultiCovered":

        set =TLObject .read (b )

        covers =TLObject .read (b )

        return StickerSetMultiCovered (set =set ,covers =covers )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .set .write ())

        b .write (Vector (self .covers ))

        return b .getvalue ()
