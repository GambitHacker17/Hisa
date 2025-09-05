
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChatAdminsWithInvites (TLObject ):
    """"""

    __slots__ :List [str ]=["admins","users"]

    ID =0xb69b72d7 
    QUALNAME ="types.messages.ChatAdminsWithInvites"

    def __init__ (self ,*,admins :List ["raw.base.ChatAdminWithInvites"],users :List ["raw.base.User"])->None :
        self .admins =admins 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChatAdminsWithInvites":

        admins =TLObject .read (b )

        users =TLObject .read (b )

        return ChatAdminsWithInvites (admins =admins ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .admins ))

        b .write (Vector (self .users ))

        return b .getvalue ()
