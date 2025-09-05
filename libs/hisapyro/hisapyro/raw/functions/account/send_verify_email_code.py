
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SendVerifyEmailCode (TLObject ):
    """"""

    __slots__ :List [str ]=["purpose","email"]

    ID =0x98e037bb 
    QUALNAME ="functions.account.SendVerifyEmailCode"

    def __init__ (self ,*,purpose :"raw.base.EmailVerifyPurpose",email :str )->None :
        self .purpose =purpose 
        self .email =email 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SendVerifyEmailCode":

        purpose =TLObject .read (b )

        email =String .read (b )

        return SendVerifyEmailCode (purpose =purpose ,email =email )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .purpose .write ())

        b .write (String (self .email ))

        return b .getvalue ()
