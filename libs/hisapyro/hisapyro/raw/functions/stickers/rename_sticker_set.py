
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class RenameStickerSet (TLObject ):
    """"""

    __slots__ :List [str ]=["stickerset","title"]

    ID =0x124b1c00 
    QUALNAME ="functions.stickers.RenameStickerSet"

    def __init__ (self ,*,stickerset :"raw.base.InputStickerSet",title :str )->None :
        self .stickerset =stickerset 
        self .title =title 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"RenameStickerSet":

        stickerset =TLObject .read (b )

        title =String .read (b )

        return RenameStickerSet (stickerset =stickerset ,title =title )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .stickerset .write ())

        b .write (String (self .title ))

        return b .getvalue ()
