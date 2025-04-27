
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ExportedInvites (TLObject ):
    """"""

    __slots__ :List [str ]=["invites","chats","users"]

    ID =0x10ab6dc7 
    QUALNAME ="types.chatlists.ExportedInvites"

    def __init__ (self ,*,invites :List ["raw.base.ExportedChatlistInvite"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"])->None :
        self .invites =invites 
        self .chats =chats 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ExportedInvites":

        invites =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return ExportedInvites (invites =invites ,chats =chats ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .invites ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
