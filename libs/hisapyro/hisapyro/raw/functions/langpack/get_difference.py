
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetDifference (TLObject ):
    """"""

    __slots__ :List [str ]=["lang_pack","lang_code","from_version"]

    ID =0xcd984aa5 
    QUALNAME ="functions.langpack.GetDifference"

    def __init__ (self ,*,lang_pack :str ,lang_code :str ,from_version :int )->None :
        self .lang_pack =lang_pack 
        self .lang_code =lang_code 
        self .from_version =from_version 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetDifference":

        lang_pack =String .read (b )

        lang_code =String .read (b )

        from_version =Int .read (b )

        return GetDifference (lang_pack =lang_pack ,lang_code =lang_code ,from_version =from_version )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .lang_pack ))

        b .write (String (self .lang_code ))

        b .write (Int (self .from_version ))

        return b .getvalue ()
