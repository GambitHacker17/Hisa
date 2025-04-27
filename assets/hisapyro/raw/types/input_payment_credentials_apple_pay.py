
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputPaymentCredentialsApplePay (TLObject ):
    """"""

    __slots__ :List [str ]=["payment_data"]

    ID =0xaa1c39f 
    QUALNAME ="types.InputPaymentCredentialsApplePay"

    def __init__ (self ,*,payment_data :"raw.base.DataJSON")->None :
        self .payment_data =payment_data 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputPaymentCredentialsApplePay":

        payment_data =TLObject .read (b )

        return InputPaymentCredentialsApplePay (payment_data =payment_data )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .payment_data .write ())

        return b .getvalue ()
