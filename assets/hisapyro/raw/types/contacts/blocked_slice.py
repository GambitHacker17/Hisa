
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class BlockedSlice (TLObject ):
    """"""

    __slots__ :List [str ]=["count","blocked","chats","users"]

    ID =0xe1664194 
    QUALNAME ="types.contacts.BlockedSlice"

    def __init__ (self ,*,count :int ,blocked :List ["raw.base.PeerBlocked"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"])->None :
        self .count =count 
        self .blocked =blocked 
        self .chats =chats 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"BlockedSlice":

        count =Int .read (b )

        blocked =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return BlockedSlice (count =count ,blocked =blocked ,chats =chats ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .count ))

        b .write (Vector (self .blocked ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
