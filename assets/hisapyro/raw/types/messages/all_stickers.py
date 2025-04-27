
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AllStickers (TLObject ):
    """"""

    __slots__ :List [str ]=["hash","sets"]

    ID =0xcdbbcebb 
    QUALNAME ="types.messages.AllStickers"

    def __init__ (self ,*,hash :int ,sets :List ["raw.base.StickerSet"])->None :
        self .hash =hash 
        self .sets =sets 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AllStickers":

        hash =Long .read (b )

        sets =TLObject .read (b )

        return AllStickers (hash =hash ,sets =sets )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .hash ))

        b .write (Vector (self .sets ))

        return b .getvalue ()
