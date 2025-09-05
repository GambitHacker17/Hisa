
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SendChangePhoneCode (TLObject ):
    """"""

    __slots__ :List [str ]=["phone_number","settings"]

    ID =0x82574ae5 
    QUALNAME ="functions.account.SendChangePhoneCode"

    def __init__ (self ,*,phone_number :str ,settings :"raw.base.CodeSettings")->None :
        self .phone_number =phone_number 
        self .settings =settings 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SendChangePhoneCode":

        phone_number =String .read (b )

        settings =TLObject .read (b )

        return SendChangePhoneCode (phone_number =phone_number ,settings =settings )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .phone_number ))

        b .write (self .settings .write ())

        return b .getvalue ()
