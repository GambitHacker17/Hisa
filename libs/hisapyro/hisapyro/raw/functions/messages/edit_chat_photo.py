
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EditChatPhoto (TLObject ):
    """"""

    __slots__ :List [str ]=["chat_id","photo"]

    ID =0x35ddd674 
    QUALNAME ="functions.messages.EditChatPhoto"

    def __init__ (self ,*,chat_id :int ,photo :"raw.base.InputChatPhoto")->None :
        self .chat_id =chat_id 
        self .photo =photo 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EditChatPhoto":

        chat_id =Long .read (b )

        photo =TLObject .read (b )

        return EditChatPhoto (chat_id =chat_id ,photo =photo )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .chat_id ))

        b .write (self .photo .write ())

        return b .getvalue ()
