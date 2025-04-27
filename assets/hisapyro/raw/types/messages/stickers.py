
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Stickers (TLObject ):
    """"""

    __slots__ :List [str ]=["hash","stickers"]

    ID =0x30a6ec7e 
    QUALNAME ="types.messages.Stickers"

    def __init__ (self ,*,hash :int ,stickers :List ["raw.base.Document"])->None :
        self .hash =hash 
        self .stickers =stickers 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Stickers":

        hash =Long .read (b )

        stickers =TLObject .read (b )

        return Stickers (hash =hash ,stickers =stickers )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .hash ))

        b .write (Vector (self .stickers ))

        return b .getvalue ()
