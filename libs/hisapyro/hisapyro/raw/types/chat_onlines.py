
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChatOnlines (TLObject ):
    """"""

    __slots__ :List [str ]=["onlines"]

    ID =0xf041e250 
    QUALNAME ="types.ChatOnlines"

    def __init__ (self ,*,onlines :int )->None :
        self .onlines =onlines 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChatOnlines":

        onlines =Int .read (b )

        return ChatOnlines (onlines =onlines )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .onlines ))

        return b .getvalue ()
