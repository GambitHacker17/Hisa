
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SignIn (TLObject ):
    """"""

    __slots__ :List [str ]=["phone_number","phone_code_hash","phone_code","email_verification"]

    ID =0x8d52a951 
    QUALNAME ="functions.auth.SignIn"

    def __init__ (self ,*,phone_number :str ,phone_code_hash :str ,phone_code :Optional [str ]=None ,email_verification :"raw.base.EmailVerification"=None )->None :
        self .phone_number =phone_number 
        self .phone_code_hash =phone_code_hash 
        self .phone_code =phone_code 
        self .email_verification =email_verification 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SignIn":

        flags =Int .read (b )

        phone_number =String .read (b )

        phone_code_hash =String .read (b )

        phone_code =String .read (b )if flags &(1 <<0 )else None 
        email_verification =TLObject .read (b )if flags &(1 <<1 )else None 

        return SignIn (phone_number =phone_number ,phone_code_hash =phone_code_hash ,phone_code =phone_code ,email_verification =email_verification )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .phone_code is not None else 0 
        flags |=(1 <<1 )if self .email_verification is not None else 0 
        b .write (Int (flags ))

        b .write (String (self .phone_number ))

        b .write (String (self .phone_code_hash ))

        if self .phone_code is not None :
            b .write (String (self .phone_code ))

        if self .email_verification is not None :
            b .write (self .email_verification .write ())

        return b .getvalue ()
