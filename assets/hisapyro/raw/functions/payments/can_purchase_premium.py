
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class CanPurchasePremium (TLObject ):
    """"""

    __slots__ :List [str ]=["purpose"]

    ID =0x9fc19eb6 
    QUALNAME ="functions.payments.CanPurchasePremium"

    def __init__ (self ,*,purpose :"raw.base.InputStorePaymentPurpose")->None :
        self .purpose =purpose 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"CanPurchasePremium":

        purpose =TLObject .read (b )

        return CanPurchasePremium (purpose =purpose )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .purpose .write ())

        return b .getvalue ()
