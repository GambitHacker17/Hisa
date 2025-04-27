
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputStorePaymentGiftPremium (TLObject ):
    """"""

    __slots__ :List [str ]=["user_id","currency","amount"]

    ID =0x616f7fe8 
    QUALNAME ="types.InputStorePaymentGiftPremium"

    def __init__ (self ,*,user_id :"raw.base.InputUser",currency :str ,amount :int )->None :
        self .user_id =user_id 
        self .currency =currency 
        self .amount =amount 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputStorePaymentGiftPremium":

        user_id =TLObject .read (b )

        currency =String .read (b )

        amount =Long .read (b )

        return InputStorePaymentGiftPremium (user_id =user_id ,currency =currency ,amount =amount )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .user_id .write ())

        b .write (String (self .currency ))

        b .write (Long (self .amount ))

        return b .getvalue ()
