
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EditChatTitle (TLObject ):
    """"""

    __slots__ :List [str ]=["chat_id","title"]

    ID =0x73783ffd 
    QUALNAME ="functions.messages.EditChatTitle"

    def __init__ (self ,*,chat_id :int ,title :str )->None :
        self .chat_id =chat_id 
        self .title =title 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EditChatTitle":

        chat_id =Long .read (b )

        title =String .read (b )

        return EditChatTitle (chat_id =chat_id ,title =title )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .chat_id ))

        b .write (String (self .title ))

        return b .getvalue ()
