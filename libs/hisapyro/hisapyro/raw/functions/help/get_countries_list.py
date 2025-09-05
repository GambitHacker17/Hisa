
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetCountriesList (TLObject ):
    """"""

    __slots__ :List [str ]=["lang_code","hash"]

    ID =0x735787a8 
    QUALNAME ="functions.help.GetCountriesList"

    def __init__ (self ,*,lang_code :str ,hash :int )->None :
        self .lang_code =lang_code 
        self .hash =hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetCountriesList":

        lang_code =String .read (b )

        hash =Int .read (b )

        return GetCountriesList (lang_code =lang_code ,hash =hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .lang_code ))

        b .write (Int (self .hash ))

        return b .getvalue ()
