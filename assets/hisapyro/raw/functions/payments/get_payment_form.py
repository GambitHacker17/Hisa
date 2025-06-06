
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetPaymentForm (TLObject ):
    """"""

    __slots__ :List [str ]=["invoice","theme_params"]

    ID =0x37148dbb 
    QUALNAME ="functions.payments.GetPaymentForm"

    def __init__ (self ,*,invoice :"raw.base.InputInvoice",theme_params :"raw.base.DataJSON"=None )->None :
        self .invoice =invoice 
        self .theme_params =theme_params 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetPaymentForm":

        flags =Int .read (b )

        invoice =TLObject .read (b )

        theme_params =TLObject .read (b )if flags &(1 <<0 )else None 

        return GetPaymentForm (invoice =invoice ,theme_params =theme_params )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .theme_params is not None else 0 
        b .write (Int (flags ))

        b .write (self .invoice .write ())

        if self .theme_params is not None :
            b .write (self .theme_params .write ())

        return b .getvalue ()
