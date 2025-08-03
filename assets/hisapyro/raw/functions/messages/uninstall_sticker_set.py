
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UninstallStickerSet (TLObject ):
    """"""

    __slots__ :List [str ]=["stickerset"]

    ID =0xf96e55de 
    QUALNAME ="functions.messages.UninstallStickerSet"

    def __init__ (self ,*,stickerset :"raw.base.InputStickerSet")->None :
        self .stickerset =stickerset 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UninstallStickerSet":

        stickerset =TLObject .read (b )

        return UninstallStickerSet (stickerset =stickerset )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .stickerset .write ())

        return b .getvalue ()
