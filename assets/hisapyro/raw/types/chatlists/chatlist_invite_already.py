
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChatlistInviteAlready (TLObject ):
    """"""

    __slots__ :List [str ]=["filter_id","missing_peers","already_peers","chats","users"]

    ID =0xfa87f659 
    QUALNAME ="types.chatlists.ChatlistInviteAlready"

    def __init__ (self ,*,filter_id :int ,missing_peers :List ["raw.base.Peer"],already_peers :List ["raw.base.Peer"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"])->None :
        self .filter_id =filter_id 
        self .missing_peers =missing_peers 
        self .already_peers =already_peers 
        self .chats =chats 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChatlistInviteAlready":

        filter_id =Int .read (b )

        missing_peers =TLObject .read (b )

        already_peers =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return ChatlistInviteAlready (filter_id =filter_id ,missing_peers =missing_peers ,already_peers =already_peers ,chats =chats ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .filter_id ))

        b .write (Vector (self .missing_peers ))

        b .write (Vector (self .already_peers ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
