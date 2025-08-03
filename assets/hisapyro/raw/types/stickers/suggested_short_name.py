
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SuggestedShortName (TLObject ):
    """"""

    __slots__ :List [str ]=["short_name"]

    ID =0x85fea03f 
    QUALNAME ="types.stickers.SuggestedShortName"

    def __init__ (self ,*,short_name :str )->None :
        self .short_name =short_name 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SuggestedShortName":

        short_name =String .read (b )

        return SuggestedShortName (short_name =short_name )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .short_name ))

        return b .getvalue ()
