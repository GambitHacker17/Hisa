
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PaymentFormMethod (TLObject ):
    """"""

    __slots__ :List [str ]=["url","title"]

    ID =0x88f8f21b 
    QUALNAME ="types.PaymentFormMethod"

    def __init__ (self ,*,url :str ,title :str )->None :
        self .url =url 
        self .title =title 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PaymentFormMethod":

        url =String .read (b )

        title =String .read (b )

        return PaymentFormMethod (url =url ,title =title )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .url ))

        b .write (String (self .title ))

        return b .getvalue ()
