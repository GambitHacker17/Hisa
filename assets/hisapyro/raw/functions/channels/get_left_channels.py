
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetLeftChannels (TLObject ):
    """"""

    __slots__ :List [str ]=["offset"]

    ID =0x8341ecc0 
    QUALNAME ="functions.channels.GetLeftChannels"

    def __init__ (self ,*,offset :int )->None :
        self .offset =offset 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetLeftChannels":

        offset =Int .read (b )

        return GetLeftChannels (offset =offset )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .offset ))

        return b .getvalue ()
