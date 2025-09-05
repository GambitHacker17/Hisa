
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AssignAppStoreTransaction (TLObject ):
    """"""

    __slots__ :List [str ]=["receipt","purpose"]

    ID =0x80ed747d 
    QUALNAME ="functions.payments.AssignAppStoreTransaction"

    def __init__ (self ,*,receipt :bytes ,purpose :"raw.base.InputStorePaymentPurpose")->None :
        self .receipt =receipt 
        self .purpose =purpose 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AssignAppStoreTransaction":

        receipt =Bytes .read (b )

        purpose =TLObject .read (b )

        return AssignAppStoreTransaction (receipt =receipt ,purpose =purpose )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Bytes (self .receipt ))

        b .write (self .purpose .write ())

        return b .getvalue ()
