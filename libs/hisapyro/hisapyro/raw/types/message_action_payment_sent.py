
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageActionPaymentSent (TLObject ):
    """"""

    __slots__ :List [str ]=["currency","total_amount","recurring_init","recurring_used","invoice_slug"]

    ID =0x96163f56 
    QUALNAME ="types.MessageActionPaymentSent"

    def __init__ (self ,*,currency :str ,total_amount :int ,recurring_init :Optional [bool ]=None ,recurring_used :Optional [bool ]=None ,invoice_slug :Optional [str ]=None )->None :
        self .currency =currency 
        self .total_amount =total_amount 
        self .recurring_init =recurring_init 
        self .recurring_used =recurring_used 
        self .invoice_slug =invoice_slug 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageActionPaymentSent":

        flags =Int .read (b )

        recurring_init =True if flags &(1 <<2 )else False 
        recurring_used =True if flags &(1 <<3 )else False 
        currency =String .read (b )

        total_amount =Long .read (b )

        invoice_slug =String .read (b )if flags &(1 <<0 )else None 
        return MessageActionPaymentSent (currency =currency ,total_amount =total_amount ,recurring_init =recurring_init ,recurring_used =recurring_used ,invoice_slug =invoice_slug )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<2 )if self .recurring_init else 0 
        flags |=(1 <<3 )if self .recurring_used else 0 
        flags |=(1 <<0 )if self .invoice_slug is not None else 0 
        b .write (Int (flags ))

        b .write (String (self .currency ))

        b .write (Long (self .total_amount ))

        if self .invoice_slug is not None :
            b .write (String (self .invoice_slug ))

        return b .getvalue ()
