
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageEntityUnknown (TLObject ):
    """"""

    __slots__ :List [str ]=["offset","length"]

    ID =0xbb92ba95 
    QUALNAME ="types.MessageEntityUnknown"

    def __init__ (self ,*,offset :int ,length :int )->None :
        self .offset =offset 
        self .length =length 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageEntityUnknown":

        offset =Int .read (b )

        length =Int .read (b )

        return MessageEntityUnknown (offset =offset ,length =length )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .offset ))

        b .write (Int (self .length ))

        return b .getvalue ()
