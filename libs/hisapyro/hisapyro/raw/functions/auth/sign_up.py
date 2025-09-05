
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SignUp (TLObject ):
    """"""

    __slots__ :List [str ]=["phone_number","phone_code_hash","first_name","last_name"]

    ID =0x80eee427 
    QUALNAME ="functions.auth.SignUp"

    def __init__ (self ,*,phone_number :str ,phone_code_hash :str ,first_name :str ,last_name :str )->None :
        self .phone_number =phone_number 
        self .phone_code_hash =phone_code_hash 
        self .first_name =first_name 
        self .last_name =last_name 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SignUp":

        phone_number =String .read (b )

        phone_code_hash =String .read (b )

        first_name =String .read (b )

        last_name =String .read (b )

        return SignUp (phone_number =phone_number ,phone_code_hash =phone_code_hash ,first_name =first_name ,last_name =last_name )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .phone_number ))

        b .write (String (self .phone_code_hash ))

        b .write (String (self .first_name ))

        b .write (String (self .last_name ))

        return b .getvalue ()
