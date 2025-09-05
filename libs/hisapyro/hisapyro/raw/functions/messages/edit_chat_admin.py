
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EditChatAdmin (TLObject ):
    """"""

    __slots__ :List [str ]=["chat_id","user_id","is_admin"]

    ID =0xa85bd1c2 
    QUALNAME ="functions.messages.EditChatAdmin"

    def __init__ (self ,*,chat_id :int ,user_id :"raw.base.InputUser",is_admin :bool )->None :
        self .chat_id =chat_id 
        self .user_id =user_id 
        self .is_admin =is_admin 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EditChatAdmin":

        chat_id =Long .read (b )

        user_id =TLObject .read (b )

        is_admin =Bool .read (b )

        return EditChatAdmin (chat_id =chat_id ,user_id =user_id ,is_admin =is_admin )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .chat_id ))

        b .write (self .user_id .write ())

        b .write (Bool (self .is_admin ))

        return b .getvalue ()
