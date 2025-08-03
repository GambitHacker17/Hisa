
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class BotInlineMessageMediaContact (TLObject ):
    """"""

    __slots__ :List [str ]=["phone_number","first_name","last_name","vcard","reply_markup"]

    ID =0x18d1cdc2 
    QUALNAME ="types.BotInlineMessageMediaContact"

    def __init__ (self ,*,phone_number :str ,first_name :str ,last_name :str ,vcard :str ,reply_markup :"raw.base.ReplyMarkup"=None )->None :
        self .phone_number =phone_number 
        self .first_name =first_name 
        self .last_name =last_name 
        self .vcard =vcard 
        self .reply_markup =reply_markup 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"BotInlineMessageMediaContact":

        flags =Int .read (b )

        phone_number =String .read (b )

        first_name =String .read (b )

        last_name =String .read (b )

        vcard =String .read (b )

        reply_markup =TLObject .read (b )if flags &(1 <<2 )else None 

        return BotInlineMessageMediaContact (phone_number =phone_number ,first_name =first_name ,last_name =last_name ,vcard =vcard ,reply_markup =reply_markup )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<2 )if self .reply_markup is not None else 0 
        b .write (Int (flags ))

        b .write (String (self .phone_number ))

        b .write (String (self .first_name ))

        b .write (String (self .last_name ))

        b .write (String (self .vcard ))

        if self .reply_markup is not None :
            b .write (self .reply_markup .write ())

        return b .getvalue ()
