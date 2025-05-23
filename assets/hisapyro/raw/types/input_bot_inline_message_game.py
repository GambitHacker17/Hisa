
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputBotInlineMessageGame (TLObject ):
    """"""

    __slots__ :List [str ]=["reply_markup"]

    ID =0x4b425864 
    QUALNAME ="types.InputBotInlineMessageGame"

    def __init__ (self ,*,reply_markup :"raw.base.ReplyMarkup"=None )->None :
        self .reply_markup =reply_markup 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputBotInlineMessageGame":

        flags =Int .read (b )

        reply_markup =TLObject .read (b )if flags &(1 <<2 )else None 

        return InputBotInlineMessageGame (reply_markup =reply_markup )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<2 )if self .reply_markup is not None else 0 
        b .write (Int (flags ))

        if self .reply_markup is not None :
            b .write (self .reply_markup .write ())

        return b .getvalue ()
