
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageEntityUnderline (TLObject ):
    """"""

    __slots__ :List [str ]=["offset","length"]

    ID =0x9c4e7e8b 
    QUALNAME ="types.MessageEntityUnderline"

    def __init__ (self ,*,offset :int ,length :int )->None :
        self .offset =offset 
        self .length =length 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageEntityUnderline":

        offset =Int .read (b )

        length =Int .read (b )

        return MessageEntityUnderline (offset =offset ,length =length )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .offset ))

        b .write (Int (self .length ))

        return b .getvalue ()
