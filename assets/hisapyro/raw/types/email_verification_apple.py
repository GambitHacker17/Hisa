
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EmailVerificationApple (TLObject ):
    """"""

    __slots__ :List [str ]=["token"]

    ID =0x96d074fd 
    QUALNAME ="types.EmailVerificationApple"

    def __init__ (self ,*,token :str )->None :
        self .token =token 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EmailVerificationApple":

        token =String .read (b )

        return EmailVerificationApple (token =token )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .token ))

        return b .getvalue ()
