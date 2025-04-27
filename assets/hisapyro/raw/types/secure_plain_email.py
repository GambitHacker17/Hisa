
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SecurePlainEmail (TLObject ):
    """"""

    __slots__ :List [str ]=["email"]

    ID =0x21ec5a5f 
    QUALNAME ="types.SecurePlainEmail"

    def __init__ (self ,*,email :str )->None :
        self .email =email 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SecurePlainEmail":

        email =String .read (b )

        return SecurePlainEmail (email =email )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .email ))

        return b .getvalue ()
