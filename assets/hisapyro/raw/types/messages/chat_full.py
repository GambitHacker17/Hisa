
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChatFull (TLObject ):
    """"""

    __slots__ :List [str ]=["full_chat","chats","users"]

    ID =0xe5d7d19c 
    QUALNAME ="types.messages.ChatFull"

    def __init__ (self ,*,full_chat :"raw.base.ChatFull",chats :List ["raw.base.Chat"],users :List ["raw.base.User"])->None :
        self .full_chat =full_chat 
        self .chats =chats 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChatFull":

        full_chat =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return ChatFull (full_chat =full_chat ,chats =chats ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .full_chat .write ())

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
