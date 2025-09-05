
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EmojiGroups (TLObject ):
    """"""

    __slots__ :List [str ]=["hash","groups"]

    ID =0x881fb94b 
    QUALNAME ="types.messages.EmojiGroups"

    def __init__ (self ,*,hash :int ,groups :List ["raw.base.EmojiGroup"])->None :
        self .hash =hash 
        self .groups =groups 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EmojiGroups":

        hash =Int .read (b )

        groups =TLObject .read (b )

        return EmojiGroups (hash =hash ,groups =groups )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .hash ))

        b .write (Vector (self .groups ))

        return b .getvalue ()
