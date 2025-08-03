
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class VerifyPhone (TLObject ):
    """"""

    __slots__ :List [str ]=["phone_number","phone_code_hash","phone_code"]

    ID =0x4dd3a7f6 
    QUALNAME ="functions.account.VerifyPhone"

    def __init__ (self ,*,phone_number :str ,phone_code_hash :str ,phone_code :str )->None :
        self .phone_number =phone_number 
        self .phone_code_hash =phone_code_hash 
        self .phone_code =phone_code 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"VerifyPhone":

        phone_number =String .read (b )

        phone_code_hash =String .read (b )

        phone_code =String .read (b )

        return VerifyPhone (phone_number =phone_number ,phone_code_hash =phone_code_hash ,phone_code =phone_code )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .phone_number ))

        b .write (String (self .phone_code_hash ))

        b .write (String (self .phone_code ))

        return b .getvalue ()
