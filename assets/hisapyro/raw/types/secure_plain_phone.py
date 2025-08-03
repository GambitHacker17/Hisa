
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SecurePlainPhone (TLObject ):
    """"""

    __slots__ :List [str ]=["phone"]

    ID =0x7d6099dd 
    QUALNAME ="types.SecurePlainPhone"

    def __init__ (self ,*,phone :str )->None :
        self .phone =phone 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SecurePlainPhone":

        phone =String .read (b )

        return SecurePlainPhone (phone =phone )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .phone ))

        return b .getvalue ()
