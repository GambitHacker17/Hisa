
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class LangPackDifference (TLObject ):
    """"""

    __slots__ :List [str ]=["lang_code","from_version","version","strings"]

    ID =0xf385c1f6 
    QUALNAME ="types.LangPackDifference"

    def __init__ (self ,*,lang_code :str ,from_version :int ,version :int ,strings :List ["raw.base.LangPackString"])->None :
        self .lang_code =lang_code 
        self .from_version =from_version 
        self .version =version 
        self .strings =strings 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"LangPackDifference":

        lang_code =String .read (b )

        from_version =Int .read (b )

        version =Int .read (b )

        strings =TLObject .read (b )

        return LangPackDifference (lang_code =lang_code ,from_version =from_version ,version =version ,strings =strings )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .lang_code ))

        b .write (Int (self .from_version ))

        b .write (Int (self .version ))

        b .write (Vector (self .strings ))

        return b .getvalue ()
