
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EmojiURL (TLObject ):
    """"""

    __slots__ :List [str ]=["url"]

    ID =0xa575739d 
    QUALNAME ="types.EmojiURL"

    def __init__ (self ,*,url :str )->None :
        self .url =url 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EmojiURL":

        url =String .read (b )

        return EmojiURL (url =url )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .url ))

        return b .getvalue ()
