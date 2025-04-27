
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class FeaturedStickers (TLObject ):
    """"""

    __slots__ :List [str ]=["hash","count","sets","unread","premium"]

    ID =0xbe382906 
    QUALNAME ="types.messages.FeaturedStickers"

    def __init__ (self ,*,hash :int ,count :int ,sets :List ["raw.base.StickerSetCovered"],unread :List [int ],premium :Optional [bool ]=None )->None :
        self .hash =hash 
        self .count =count 
        self .sets =sets 
        self .unread =unread 
        self .premium =premium 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"FeaturedStickers":

        flags =Int .read (b )

        premium =True if flags &(1 <<0 )else False 
        hash =Long .read (b )

        count =Int .read (b )

        sets =TLObject .read (b )

        unread =TLObject .read (b ,Long )

        return FeaturedStickers (hash =hash ,count =count ,sets =sets ,unread =unread ,premium =premium )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .premium else 0 
        b .write (Int (flags ))

        b .write (Long (self .hash ))

        b .write (Int (self .count ))

        b .write (Vector (self .sets ))

        b .write (Vector (self .unread ,Long ))

        return b .getvalue ()
