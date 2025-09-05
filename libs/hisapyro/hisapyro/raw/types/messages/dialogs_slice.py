
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DialogsSlice (TLObject ):
    """"""

    __slots__ :List [str ]=["count","dialogs","messages","chats","users"]

    ID =0x71e094f3 
    QUALNAME ="types.messages.DialogsSlice"

    def __init__ (self ,*,count :int ,dialogs :List ["raw.base.Dialog"],messages :List ["raw.base.Message"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"])->None :
        self .count =count 
        self .dialogs =dialogs 
        self .messages =messages 
        self .chats =chats 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DialogsSlice":

        count =Int .read (b )

        dialogs =TLObject .read (b )

        messages =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return DialogsSlice (count =count ,dialogs =dialogs ,messages =messages ,chats =chats ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .count ))

        b .write (Vector (self .dialogs ))

        b .write (Vector (self .messages ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
