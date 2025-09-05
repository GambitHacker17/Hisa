
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ExportedChatInvite (TLObject ):
    """"""

    __slots__ :List [str ]=["invite","users"]

    ID =0x1871be50 
    QUALNAME ="types.messages.ExportedChatInvite"

    def __init__ (self ,*,invite :"raw.base.ExportedChatInvite",users :List ["raw.base.User"])->None :
        self .invite =invite 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ExportedChatInvite":

        invite =TLObject .read (b )

        users =TLObject .read (b )

        return ExportedChatInvite (invite =invite ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .invite .write ())

        b .write (Vector (self .users ))

        return b .getvalue ()
