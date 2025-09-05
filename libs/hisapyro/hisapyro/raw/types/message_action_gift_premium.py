
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageActionGiftPremium (TLObject ):
    """"""

    __slots__ :List [str ]=["currency","amount","months","crypto_currency","crypto_amount"]

    ID =0xc83d6aec 
    QUALNAME ="types.MessageActionGiftPremium"

    def __init__ (self ,*,currency :str ,amount :int ,months :int ,crypto_currency :Optional [str ]=None ,crypto_amount :Optional [int ]=None )->None :
        self .currency =currency 
        self .amount =amount 
        self .months =months 
        self .crypto_currency =crypto_currency 
        self .crypto_amount =crypto_amount 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageActionGiftPremium":

        flags =Int .read (b )

        currency =String .read (b )

        amount =Long .read (b )

        months =Int .read (b )

        crypto_currency =String .read (b )if flags &(1 <<0 )else None 
        crypto_amount =Long .read (b )if flags &(1 <<0 )else None 
        return MessageActionGiftPremium (currency =currency ,amount =amount ,months =months ,crypto_currency =crypto_currency ,crypto_amount =crypto_amount )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .crypto_currency is not None else 0 
        flags |=(1 <<0 )if self .crypto_amount is not None else 0 
        b .write (Int (flags ))

        b .write (String (self .currency ))

        b .write (Long (self .amount ))

        b .write (Int (self .months ))

        if self .crypto_currency is not None :
            b .write (String (self .crypto_currency ))

        if self .crypto_amount is not None :
            b .write (Long (self .crypto_amount ))

        return b .getvalue ()
