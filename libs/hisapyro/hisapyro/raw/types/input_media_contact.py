
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputMediaContact (TLObject ):
    """"""

    __slots__ :List [str ]=["phone_number","first_name","last_name","vcard"]

    ID =0xf8ab7dfb 
    QUALNAME ="types.InputMediaContact"

    def __init__ (self ,*,phone_number :str ,first_name :str ,last_name :str ,vcard :str )->None :
        self .phone_number =phone_number 
        self .first_name =first_name 
        self .last_name =last_name 
        self .vcard =vcard 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputMediaContact":

        phone_number =String .read (b )

        first_name =String .read (b )

        last_name =String .read (b )

        vcard =String .read (b )

        return InputMediaContact (phone_number =phone_number ,first_name =first_name ,last_name =last_name ,vcard =vcard )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .phone_number ))

        b .write (String (self .first_name ))

        b .write (String (self .last_name ))

        b .write (String (self .vcard ))

        return b .getvalue ()
