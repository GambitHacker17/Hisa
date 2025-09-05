
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ExportInvoice (TLObject ):
    """"""

    __slots__ :List [str ]=["invoice_media"]

    ID =0xf91b065 
    QUALNAME ="functions.payments.ExportInvoice"

    def __init__ (self ,*,invoice_media :"raw.base.InputMedia")->None :
        self .invoice_media =invoice_media 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ExportInvoice":

        invoice_media =TLObject .read (b )

        return ExportInvoice (invoice_media =invoice_media )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .invoice_media .write ())

        return b .getvalue ()
