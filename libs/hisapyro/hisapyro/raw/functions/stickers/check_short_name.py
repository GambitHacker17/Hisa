
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class CheckShortName (TLObject ):
    """"""

    __slots__ :List [str ]=["short_name"]

    ID =0x284b3639 
    QUALNAME ="functions.stickers.CheckShortName"

    def __init__ (self ,*,short_name :str )->None :
        self .short_name =short_name 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"CheckShortName":

        short_name =String .read (b )

        return CheckShortName (short_name =short_name )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .short_name ))

        return b .getvalue ()
