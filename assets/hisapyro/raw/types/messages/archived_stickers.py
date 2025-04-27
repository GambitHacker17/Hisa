
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ArchivedStickers (TLObject ):
    """"""

    __slots__ :List [str ]=["count","sets"]

    ID =0x4fcba9c8 
    QUALNAME ="types.messages.ArchivedStickers"

    def __init__ (self ,*,count :int ,sets :List ["raw.base.StickerSetCovered"])->None :
        self .count =count 
        self .sets =sets 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ArchivedStickers":

        count =Int .read (b )

        sets =TLObject .read (b )

        return ArchivedStickers (count =count ,sets =sets )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .count ))

        b .write (Vector (self .sets ))

        return b .getvalue ()
