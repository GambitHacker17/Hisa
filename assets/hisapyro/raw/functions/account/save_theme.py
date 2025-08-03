
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SaveTheme (TLObject ):
    """"""

    __slots__ :List [str ]=["theme","unsave"]

    ID =0xf257106c 
    QUALNAME ="functions.account.SaveTheme"

    def __init__ (self ,*,theme :"raw.base.InputTheme",unsave :bool )->None :
        self .theme =theme 
        self .unsave =unsave 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SaveTheme":

        theme =TLObject .read (b )

        unsave =Bool .read (b )

        return SaveTheme (theme =theme ,unsave =unsave )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .theme .write ())

        b .write (Bool (self .unsave ))

        return b .getvalue ()
