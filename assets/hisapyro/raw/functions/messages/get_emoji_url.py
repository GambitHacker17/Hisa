
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetEmojiURL (TLObject ):
    """"""

    __slots__ :List [str ]=["lang_code"]

    ID =0xd5b10c26 
    QUALNAME ="functions.messages.GetEmojiURL"

    def __init__ (self ,*,lang_code :str )->None :
        self .lang_code =lang_code 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetEmojiURL":

        lang_code =String .read (b )

        return GetEmojiURL (lang_code =lang_code )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .lang_code ))

        return b .getvalue ()
