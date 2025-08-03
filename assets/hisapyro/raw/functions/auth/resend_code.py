
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ResendCode (TLObject ):
    """"""

    __slots__ :List [str ]=["phone_number","phone_code_hash"]

    ID =0x3ef1a9bf 
    QUALNAME ="functions.auth.ResendCode"

    def __init__ (self ,*,phone_number :str ,phone_code_hash :str )->None :
        self .phone_number =phone_number 
        self .phone_code_hash =phone_code_hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ResendCode":

        phone_number =String .read (b )

        phone_code_hash =String .read (b )

        return ResendCode (phone_number =phone_number ,phone_code_hash =phone_code_hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .phone_number ))

        b .write (String (self .phone_code_hash ))

        return b .getvalue ()
