
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Blocked (TLObject ):
    """"""

    __slots__ :List [str ]=["blocked","chats","users"]

    ID =0xade1591 
    QUALNAME ="types.contacts.Blocked"

    def __init__ (self ,*,blocked :List ["raw.base.PeerBlocked"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"])->None :
        self .blocked =blocked 
        self .chats =chats 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Blocked":

        blocked =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return Blocked (blocked =blocked ,chats =chats ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .blocked ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
