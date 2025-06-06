
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SendVerifyPhoneCode (TLObject ):
    """"""

    __slots__ :List [str ]=["phone_number","settings"]

    ID =0xa5a356f9 
    QUALNAME ="functions.account.SendVerifyPhoneCode"

    def __init__ (self ,*,phone_number :str ,settings :"raw.base.CodeSettings")->None :
        self .phone_number =phone_number 
        self .settings =settings 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SendVerifyPhoneCode":

        phone_number =String .read (b )

        settings =TLObject .read (b )

        return SendVerifyPhoneCode (phone_number =phone_number ,settings =settings )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .phone_number ))

        b .write (self .settings .write ())

        return b .getvalue ()
