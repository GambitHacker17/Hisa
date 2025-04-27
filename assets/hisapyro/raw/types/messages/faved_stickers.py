
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class FavedStickers (TLObject ):
    """"""

    __slots__ :List [str ]=["hash","packs","stickers"]

    ID =0x2cb51097 
    QUALNAME ="types.messages.FavedStickers"

    def __init__ (self ,*,hash :int ,packs :List ["raw.base.StickerPack"],stickers :List ["raw.base.Document"])->None :
        self .hash =hash 
        self .packs =packs 
        self .stickers =stickers 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"FavedStickers":

        hash =Long .read (b )

        packs =TLObject .read (b )

        stickers =TLObject .read (b )

        return FavedStickers (hash =hash ,packs =packs ,stickers =stickers )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .hash ))

        b .write (Vector (self .packs ))

        b .write (Vector (self .stickers ))

        return b .getvalue ()
