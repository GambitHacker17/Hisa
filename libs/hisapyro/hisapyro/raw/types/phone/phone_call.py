
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PhoneCall (TLObject ):
    """"""

    __slots__ :List [str ]=["phone_call","users"]

    ID =0xec82e140 
    QUALNAME ="types.phone.PhoneCall"

    def __init__ (self ,*,phone_call :"raw.base.PhoneCall",users :List ["raw.base.User"])->None :
        self .phone_call =phone_call 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PhoneCall":

        phone_call =TLObject .read (b )

        users =TLObject .read (b )

        return PhoneCall (phone_call =phone_call ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .phone_call .write ())

        b .write (Vector (self .users ))

        return b .getvalue ()
