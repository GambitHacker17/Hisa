
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdatePhoneCall (TLObject ):
    """"""

    __slots__ :List [str ]=["phone_call"]

    ID =0xab0f6b1e 
    QUALNAME ="types.UpdatePhoneCall"

    def __init__ (self ,*,phone_call :"raw.base.PhoneCall")->None :
        self .phone_call =phone_call 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdatePhoneCall":

        phone_call =TLObject .read (b )

        return UpdatePhoneCall (phone_call =phone_call )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .phone_call .write ())

        return b .getvalue ()
