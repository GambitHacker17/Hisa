
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetLangPack (TLObject ):
    """"""

    __slots__ :List [str ]=["lang_pack","lang_code"]

    ID =0xf2f2330a 
    QUALNAME ="functions.langpack.GetLangPack"

    def __init__ (self ,*,lang_pack :str ,lang_code :str )->None :
        self .lang_pack =lang_pack 
        self .lang_code =lang_code 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetLangPack":

        lang_pack =String .read (b )

        lang_code =String .read (b )

        return GetLangPack (lang_pack =lang_pack ,lang_code =lang_code )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .lang_pack ))

        b .write (String (self .lang_code ))

        return b .getvalue ()
