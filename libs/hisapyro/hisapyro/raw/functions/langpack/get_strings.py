
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetStrings (TLObject ):
    """"""

    __slots__ :List [str ]=["lang_pack","lang_code","keys"]

    ID =0xefea3803 
    QUALNAME ="functions.langpack.GetStrings"

    def __init__ (self ,*,lang_pack :str ,lang_code :str ,keys :List [str ])->None :
        self .lang_pack =lang_pack 
        self .lang_code =lang_code 
        self .keys =keys 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetStrings":

        lang_pack =String .read (b )

        lang_code =String .read (b )

        keys =TLObject .read (b ,String )

        return GetStrings (lang_pack =lang_pack ,lang_code =lang_code ,keys =keys )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .lang_pack ))

        b .write (String (self .lang_code ))

        b .write (Vector (self .keys ,String ))

        return b .getvalue ()
