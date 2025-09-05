
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PaymentVerificationNeeded (TLObject ):
    """"""

    __slots__ :List [str ]=["url"]

    ID =0xd8411139 
    QUALNAME ="types.payments.PaymentVerificationNeeded"

    def __init__ (self ,*,url :str )->None :
        self .url =url 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PaymentVerificationNeeded":

        url =String .read (b )

        return PaymentVerificationNeeded (url =url )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .url ))

        return b .getvalue ()
