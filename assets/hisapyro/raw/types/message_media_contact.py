
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageMediaContact (TLObject ):
    """"""

    __slots__ :List [str ]=["phone_number","first_name","last_name","vcard","user_id"]

    ID =0x70322949 
    QUALNAME ="types.MessageMediaContact"

    def __init__ (self ,*,phone_number :str ,first_name :str ,last_name :str ,vcard :str ,user_id :int )->None :
        self .phone_number =phone_number 
        self .first_name =first_name 
        self .last_name =last_name 
        self .vcard =vcard 
        self .user_id =user_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageMediaContact":

        phone_number =String .read (b )

        first_name =String .read (b )

        last_name =String .read (b )

        vcard =String .read (b )

        user_id =Long .read (b )

        return MessageMediaContact (phone_number =phone_number ,first_name =first_name ,last_name =last_name ,vcard =vcard ,user_id =user_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .phone_number ))

        b .write (String (self .first_name ))

        b .write (String (self .last_name ))

        b .write (String (self .vcard ))

        b .write (Long (self .user_id ))

        return b .getvalue ()
