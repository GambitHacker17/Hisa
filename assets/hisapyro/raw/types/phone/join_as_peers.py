
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class JoinAsPeers (TLObject ):
    """"""

    __slots__ :List [str ]=["peers","chats","users"]

    ID =0xafe5623f 
    QUALNAME ="types.phone.JoinAsPeers"

    def __init__ (self ,*,peers :List ["raw.base.Peer"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"])->None :
        self .peers =peers 
        self .chats =chats 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"JoinAsPeers":

        peers =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return JoinAsPeers (peers =peers ,chats =chats ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .peers ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
