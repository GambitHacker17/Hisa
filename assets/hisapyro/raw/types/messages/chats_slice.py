
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChatsSlice (TLObject ):
    """"""

    __slots__ :List [str ]=["count","chats"]

    ID =0x9cd81144 
    QUALNAME ="types.messages.ChatsSlice"

    def __init__ (self ,*,count :int ,chats :List ["raw.base.Chat"])->None :
        self .count =count 
        self .chats =chats 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChatsSlice":

        count =Int .read (b )

        chats =TLObject .read (b )

        return ChatsSlice (count =count ,chats =chats )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .count ))

        b .write (Vector (self .chats ))

        return b .getvalue ()
