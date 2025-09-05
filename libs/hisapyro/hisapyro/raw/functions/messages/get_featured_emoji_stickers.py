
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetFeaturedEmojiStickers (TLObject ):
    """"""

    __slots__ :List [str ]=["hash"]

    ID =0xecf6736 
    QUALNAME ="functions.messages.GetFeaturedEmojiStickers"

    def __init__ (self ,*,hash :int )->None :
        self .hash =hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetFeaturedEmojiStickers":

        hash =Long .read (b )

        return GetFeaturedEmojiStickers (hash =hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .hash ))

        return b .getvalue ()
