
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InactiveChats (TLObject ):
    """"""

    __slots__ :List [str ]=["dates","chats","users"]

    ID =0xa927fec5 
    QUALNAME ="types.messages.InactiveChats"

    def __init__ (self ,*,dates :List [int ],chats :List ["raw.base.Chat"],users :List ["raw.base.User"])->None :
        self .dates =dates 
        self .chats =chats 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InactiveChats":

        dates =TLObject .read (b ,Int )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return InactiveChats (dates =dates ,chats =chats ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .dates ,Int ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
