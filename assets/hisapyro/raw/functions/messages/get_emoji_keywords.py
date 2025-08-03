
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetEmojiKeywords (TLObject ):
    """"""

    __slots__ :List [str ]=["lang_code"]

    ID =0x35a0e062 
    QUALNAME ="functions.messages.GetEmojiKeywords"

    def __init__ (self ,*,lang_code :str )->None :
        self .lang_code =lang_code 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetEmojiKeywords":

        lang_code =String .read (b )

        return GetEmojiKeywords (lang_code =lang_code )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .lang_code ))

        return b .getvalue ()
