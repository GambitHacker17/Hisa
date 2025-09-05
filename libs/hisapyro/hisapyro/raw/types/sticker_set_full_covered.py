
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class StickerSetFullCovered (TLObject ):
    """"""

    __slots__ :List [str ]=["set","packs","keywords","documents"]

    ID =0x40d13c0e 
    QUALNAME ="types.StickerSetFullCovered"

    def __init__ (self ,*,set :"raw.base.StickerSet",packs :List ["raw.base.StickerPack"],keywords :List ["raw.base.StickerKeyword"],documents :List ["raw.base.Document"])->None :
        self .set =set 
        self .packs =packs 
        self .keywords =keywords 
        self .documents =documents 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"StickerSetFullCovered":

        set =TLObject .read (b )

        packs =TLObject .read (b )

        keywords =TLObject .read (b )

        documents =TLObject .read (b )

        return StickerSetFullCovered (set =set ,packs =packs ,keywords =keywords ,documents =documents )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .set .write ())

        b .write (Vector (self .packs ))

        b .write (Vector (self .keywords ))

        b .write (Vector (self .documents ))

        return b .getvalue ()
