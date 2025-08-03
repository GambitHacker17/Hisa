
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageExtendedMedia (TLObject ):
    """"""

    __slots__ :List [str ]=["media"]

    ID =0xee479c64 
    QUALNAME ="types.MessageExtendedMedia"

    def __init__ (self ,*,media :"raw.base.MessageMedia")->None :
        self .media =media 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageExtendedMedia":

        media =TLObject .read (b )

        return MessageExtendedMedia (media =media )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .media .write ())

        return b .getvalue ()
