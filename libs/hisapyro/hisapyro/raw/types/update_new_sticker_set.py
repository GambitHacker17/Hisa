
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateNewStickerSet (TLObject ):
    """"""

    __slots__ :List [str ]=["stickerset"]

    ID =0x688a30aa 
    QUALNAME ="types.UpdateNewStickerSet"

    def __init__ (self ,*,stickerset :"raw.base.messages.StickerSet")->None :
        self .stickerset =stickerset 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateNewStickerSet":

        stickerset =TLObject .read (b )

        return UpdateNewStickerSet (stickerset =stickerset )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .stickerset .write ())

        return b .getvalue ()
