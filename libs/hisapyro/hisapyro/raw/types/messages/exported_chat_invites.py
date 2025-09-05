
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ExportedChatInvites (TLObject ):
    """"""

    __slots__ :List [str ]=["count","invites","users"]

    ID =0xbdc62dcc 
    QUALNAME ="types.messages.ExportedChatInvites"

    def __init__ (self ,*,count :int ,invites :List ["raw.base.ExportedChatInvite"],users :List ["raw.base.User"])->None :
        self .count =count 
        self .invites =invites 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ExportedChatInvites":

        count =Int .read (b )

        invites =TLObject .read (b )

        users =TLObject .read (b )

        return ExportedChatInvites (count =count ,invites =invites ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .count ))

        b .write (Vector (self .invites ))

        b .write (Vector (self .users ))

        return b .getvalue ()
