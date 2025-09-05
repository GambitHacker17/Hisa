
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetOldFeaturedStickers (TLObject ):
    """"""

    __slots__ :List [str ]=["offset","limit","hash"]

    ID =0x7ed094a1 
    QUALNAME ="functions.messages.GetOldFeaturedStickers"

    def __init__ (self ,*,offset :int ,limit :int ,hash :int )->None :
        self .offset =offset 
        self .limit =limit 
        self .hash =hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetOldFeaturedStickers":

        offset =Int .read (b )

        limit =Int .read (b )

        hash =Long .read (b )

        return GetOldFeaturedStickers (offset =offset ,limit =limit ,hash =hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .offset ))

        b .write (Int (self .limit ))

        b .write (Long (self .hash ))

        return b .getvalue ()
