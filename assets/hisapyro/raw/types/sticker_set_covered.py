
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class StickerSetCovered (TLObject ):
    """"""

    __slots__ :List [str ]=["set","cover"]

    ID =0x6410a5d2 
    QUALNAME ="types.StickerSetCovered"

    def __init__ (self ,*,set :"raw.base.StickerSet",cover :"raw.base.Document")->None :
        self .set =set 
        self .cover =cover 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"StickerSetCovered":

        set =TLObject .read (b )

        cover =TLObject .read (b )

        return StickerSetCovered (set =set ,cover =cover )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .set .write ())

        b .write (self .cover .write ())

        return b .getvalue ()
