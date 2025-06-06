
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetStickerSet (TLObject ):
    """"""

    __slots__ :List [str ]=["stickerset","hash"]

    ID =0xc8a0ec74 
    QUALNAME ="functions.messages.GetStickerSet"

    def __init__ (self ,*,stickerset :"raw.base.InputStickerSet",hash :int )->None :
        self .stickerset =stickerset 
        self .hash =hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetStickerSet":

        stickerset =TLObject .read (b )

        hash =Int .read (b )

        return GetStickerSet (stickerset =stickerset ,hash =hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .stickerset .write ())

        b .write (Int (self .hash ))

        return b .getvalue ()
