
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PaymentResult (TLObject ):
    """"""

    __slots__ :List [str ]=["updates"]

    ID =0x4e5f810d 
    QUALNAME ="types.payments.PaymentResult"

    def __init__ (self ,*,updates :"raw.base.Updates")->None :
        self .updates =updates 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PaymentResult":

        updates =TLObject .read (b )

        return PaymentResult (updates =updates )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .updates .write ())

        return b .getvalue ()
