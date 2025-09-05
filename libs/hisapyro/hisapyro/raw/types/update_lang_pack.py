
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateLangPack (TLObject ):
    """"""

    __slots__ :List [str ]=["difference"]

    ID =0x56022f4d 
    QUALNAME ="types.UpdateLangPack"

    def __init__ (self ,*,difference :"raw.base.LangPackDifference")->None :
        self .difference =difference 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateLangPack":

        difference =TLObject .read (b )

        return UpdateLangPack (difference =difference )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .difference .write ())

        return b .getvalue ()
