
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageViews (TLObject ):
    """"""

    __slots__ :List [str ]=["views","chats","users"]

    ID =0xb6c4f543 
    QUALNAME ="types.messages.MessageViews"

    def __init__ (self ,*,views :List ["raw.base.MessageViews"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"])->None :
        self .views =views 
        self .chats =chats 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageViews":

        views =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return MessageViews (views =views ,chats =chats ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .views ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
