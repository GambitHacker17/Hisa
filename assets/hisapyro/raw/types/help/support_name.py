
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SupportName (TLObject ):
    """"""

    __slots__ :List [str ]=["name"]

    ID =0x8c05f1c9 
    QUALNAME ="types.help.SupportName"

    def __init__ (self ,*,name :str )->None :
        self .name =name 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SupportName":

        name =String .read (b )

        return SupportName (name =name )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .name ))

        return b .getvalue ()
