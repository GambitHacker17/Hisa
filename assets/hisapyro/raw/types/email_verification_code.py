
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EmailVerificationCode (TLObject ):
    """"""

    __slots__ :List [str ]=["code"]

    ID =0x922e55a9 
    QUALNAME ="types.EmailVerificationCode"

    def __init__ (self ,*,code :str )->None :
        self .code =code 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EmailVerificationCode":

        code =String .read (b )

        return EmailVerificationCode (code =code )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .code ))

        return b .getvalue ()
