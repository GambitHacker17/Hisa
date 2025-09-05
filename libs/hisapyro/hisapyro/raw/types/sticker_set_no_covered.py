
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class StickerSetNoCovered (TLObject ):
    """"""

    __slots__ :List [str ]=["set"]

    ID =0x77b15d1c 
    QUALNAME ="types.StickerSetNoCovered"

    def __init__ (self ,*,set :"raw.base.StickerSet")->None :
        self .set =set 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"StickerSetNoCovered":

        set =TLObject .read (b )

        return StickerSetNoCovered (set =set )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .set .write ())

        return b .getvalue ()
