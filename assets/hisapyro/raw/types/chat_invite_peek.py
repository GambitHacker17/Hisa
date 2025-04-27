
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChatInvitePeek (TLObject ):
    """"""

    __slots__ :List [str ]=["chat","expires"]

    ID =0x61695cb0 
    QUALNAME ="types.ChatInvitePeek"

    def __init__ (self ,*,chat :"raw.base.Chat",expires :int )->None :
        self .chat =chat 
        self .expires =expires 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChatInvitePeek":

        chat =TLObject .read (b )

        expires =Int .read (b )

        return ChatInvitePeek (chat =chat ,expires =expires )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .chat .write ())

        b .write (Int (self .expires ))

        return b .getvalue ()
