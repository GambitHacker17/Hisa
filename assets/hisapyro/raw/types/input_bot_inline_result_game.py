
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputBotInlineResultGame (TLObject ):
    """"""

    __slots__ :List [str ]=["id","short_name","send_message"]

    ID =0x4fa417f2 
    QUALNAME ="types.InputBotInlineResultGame"

    def __init__ (self ,*,id :str ,short_name :str ,send_message :"raw.base.InputBotInlineMessage")->None :
        self .id =id 
        self .short_name =short_name 
        self .send_message =send_message 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputBotInlineResultGame":

        id =String .read (b )

        short_name =String .read (b )

        send_message =TLObject .read (b )

        return InputBotInlineResultGame (id =id ,short_name =short_name ,send_message =send_message )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .id ))

        b .write (String (self .short_name ))

        b .write (self .send_message .write ())

        return b .getvalue ()
