
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class TopPeers (TLObject ):
    """"""

    __slots__ :List [str ]=["categories","chats","users"]

    ID =0x70b772a8 
    QUALNAME ="types.contacts.TopPeers"

    def __init__ (self ,*,categories :List ["raw.base.TopPeerCategoryPeers"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"])->None :
        self .categories =categories 
        self .chats =chats 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"TopPeers":

        categories =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return TopPeers (categories =categories ,chats =chats ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .categories ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
