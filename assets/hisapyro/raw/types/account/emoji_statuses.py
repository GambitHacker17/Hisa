
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EmojiStatuses (TLObject ):
    """"""

    __slots__ :List [str ]=["hash","statuses"]

    ID =0x90c467d1 
    QUALNAME ="types.account.EmojiStatuses"

    def __init__ (self ,*,hash :int ,statuses :List ["raw.base.EmojiStatus"])->None :
        self .hash =hash 
        self .statuses =statuses 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EmojiStatuses":

        hash =Long .read (b )

        statuses =TLObject .read (b )

        return EmojiStatuses (hash =hash ,statuses =statuses )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .hash ))

        b .write (Vector (self .statuses ))

        return b .getvalue ()
