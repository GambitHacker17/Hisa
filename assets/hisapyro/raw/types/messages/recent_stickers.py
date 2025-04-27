
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class RecentStickers (TLObject ):
    """"""

    __slots__ :List [str ]=["hash","packs","stickers","dates"]

    ID =0x88d37c56 
    QUALNAME ="types.messages.RecentStickers"

    def __init__ (self ,*,hash :int ,packs :List ["raw.base.StickerPack"],stickers :List ["raw.base.Document"],dates :List [int ])->None :
        self .hash =hash 
        self .packs =packs 
        self .stickers =stickers 
        self .dates =dates 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"RecentStickers":

        hash =Long .read (b )

        packs =TLObject .read (b )

        stickers =TLObject .read (b )

        dates =TLObject .read (b ,Int )

        return RecentStickers (hash =hash ,packs =packs ,stickers =stickers ,dates =dates )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .hash ))

        b .write (Vector (self .packs ))

        b .write (Vector (self .stickers ))

        b .write (Vector (self .dates ,Int ))

        return b .getvalue ()
