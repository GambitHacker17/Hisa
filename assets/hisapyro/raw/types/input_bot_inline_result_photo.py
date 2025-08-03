
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputBotInlineResultPhoto (TLObject ):
    """"""

    __slots__ :List [str ]=["id","type","photo","send_message"]

    ID =0xa8d864a7 
    QUALNAME ="types.InputBotInlineResultPhoto"

    def __init__ (self ,*,id :str ,type :str ,photo :"raw.base.InputPhoto",send_message :"raw.base.InputBotInlineMessage")->None :
        self .id =id 
        self .type =type 
        self .photo =photo 
        self .send_message =send_message 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputBotInlineResultPhoto":

        id =String .read (b )

        type =String .read (b )

        photo =TLObject .read (b )

        send_message =TLObject .read (b )

        return InputBotInlineResultPhoto (id =id ,type =type ,photo =photo ,send_message =send_message )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .id ))

        b .write (String (self .type ))

        b .write (self .photo .write ())

        b .write (self .send_message .write ())

        return b .getvalue ()
