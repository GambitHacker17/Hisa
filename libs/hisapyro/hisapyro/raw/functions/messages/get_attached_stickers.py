
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetAttachedStickers (TLObject ):
    """"""

    __slots__ :List [str ]=["media"]

    ID =0xcc5b67cc 
    QUALNAME ="functions.messages.GetAttachedStickers"

    def __init__ (self ,*,media :"raw.base.InputStickeredMedia")->None :
        self .media =media 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetAttachedStickers":

        media =TLObject .read (b )

        return GetAttachedStickers (media =media )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .media .write ())

        return b .getvalue ()
