
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetDefaultEmojiStatuses (TLObject ):
    """"""

    __slots__ :List [str ]=["hash"]

    ID =0xd6753386 
    QUALNAME ="functions.account.GetDefaultEmojiStatuses"

    def __init__ (self ,*,hash :int )->None :
        self .hash =hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetDefaultEmojiStatuses":

        hash =Long .read (b )

        return GetDefaultEmojiStatuses (hash =hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .hash ))

        return b .getvalue ()
