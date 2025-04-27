
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AddStickerToSet (TLObject ):
    """"""

    __slots__ :List [str ]=["stickerset","sticker"]

    ID =0x8653febe 
    QUALNAME ="functions.stickers.AddStickerToSet"

    def __init__ (self ,*,stickerset :"raw.base.InputStickerSet",sticker :"raw.base.InputStickerSetItem")->None :
        self .stickerset =stickerset 
        self .sticker =sticker 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AddStickerToSet":

        stickerset =TLObject .read (b )

        sticker =TLObject .read (b )

        return AddStickerToSet (stickerset =stickerset ,sticker =sticker )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .stickerset .write ())

        b .write (self .sticker .write ())

        return b .getvalue ()
