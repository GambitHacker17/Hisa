
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Messages (TLObject ):
    """"""

    __slots__ :List [str ]=["messages","chats","users"]

    ID =0x8c718e87 
    QUALNAME ="types.messages.Messages"

    def __init__ (self ,*,messages :List ["raw.base.Message"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"])->None :
        self .messages =messages 
        self .chats =chats 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Messages":

        messages =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return Messages (messages =messages ,chats =chats ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .messages ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
