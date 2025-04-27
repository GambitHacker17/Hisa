
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetLanguages (TLObject ):
    """"""

    __slots__ :List [str ]=["lang_pack"]

    ID =0x42c6978f 
    QUALNAME ="functions.langpack.GetLanguages"

    def __init__ (self ,*,lang_pack :str )->None :
        self .lang_pack =lang_pack 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetLanguages":

        lang_pack =String .read (b )

        return GetLanguages (lang_pack =lang_pack )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .lang_pack ))

        return b .getvalue ()
