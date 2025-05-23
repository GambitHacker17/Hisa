
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetTheme (TLObject ):
    """"""

    __slots__ :List [str ]=["format","theme"]

    ID =0x3a5869ec 
    QUALNAME ="functions.account.GetTheme"

    def __init__ (self ,*,format :str ,theme :"raw.base.InputTheme")->None :
        self .format =format 
        self .theme =theme 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetTheme":

        format =String .read (b )

        theme =TLObject .read (b )

        return GetTheme (format =format ,theme =theme )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .format ))

        b .write (self .theme .write ())

        return b .getvalue ()
