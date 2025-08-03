
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChatlistUpdates (TLObject ):
    """"""

    __slots__ :List [str ]=["missing_peers","chats","users"]

    ID =0x93bd878d 
    QUALNAME ="types.chatlists.ChatlistUpdates"

    def __init__ (self ,*,missing_peers :List ["raw.base.Peer"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"])->None :
        self .missing_peers =missing_peers 
        self .chats =chats 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChatlistUpdates":

        missing_peers =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return ChatlistUpdates (missing_peers =missing_peers ,chats =chats ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .missing_peers ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
