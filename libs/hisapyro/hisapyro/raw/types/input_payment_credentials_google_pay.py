
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputPaymentCredentialsGooglePay (TLObject ):
    """"""

    __slots__ :List [str ]=["payment_token"]

    ID =0x8ac32801 
    QUALNAME ="types.InputPaymentCredentialsGooglePay"

    def __init__ (self ,*,payment_token :"raw.base.DataJSON")->None :
        self .payment_token =payment_token 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputPaymentCredentialsGooglePay":

        payment_token =TLObject .read (b )

        return InputPaymentCredentialsGooglePay (payment_token =payment_token )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .payment_token .write ())

        return b .getvalue ()
