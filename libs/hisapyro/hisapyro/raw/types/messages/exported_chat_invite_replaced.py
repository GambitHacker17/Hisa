
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ExportedChatInviteReplaced (TLObject ):
    """"""

    __slots__ :List [str ]=["invite","new_invite","users"]

    ID =0x222600ef 
    QUALNAME ="types.messages.ExportedChatInviteReplaced"

    def __init__ (self ,*,invite :"raw.base.ExportedChatInvite",new_invite :"raw.base.ExportedChatInvite",users :List ["raw.base.User"])->None :
        self .invite =invite 
        self .new_invite =new_invite 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ExportedChatInviteReplaced":

        invite =TLObject .read (b )

        new_invite =TLObject .read (b )

        users =TLObject .read (b )

        return ExportedChatInviteReplaced (invite =invite ,new_invite =new_invite ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .invite .write ())

        b .write (self .new_invite .write ())

        b .write (Vector (self .users ))

        return b .getvalue ()
