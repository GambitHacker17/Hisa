
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetEmojiKeywordsLanguages (TLObject ):
    """"""

    __slots__ :List [str ]=["lang_codes"]

    ID =0x4e9963b2 
    QUALNAME ="functions.messages.GetEmojiKeywordsLanguages"

    def __init__ (self ,*,lang_codes :List [str ])->None :
        self .lang_codes =lang_codes 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetEmojiKeywordsLanguages":

        lang_codes =TLObject .read (b ,String )

        return GetEmojiKeywordsLanguages (lang_codes =lang_codes )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .lang_codes ,String ))

        return b .getvalue ()
