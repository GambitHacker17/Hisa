
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChatInviteAlready (TLObject ):
    """"""

    __slots__ :List [str ]=["chat"]

    ID =0x5a686d7c 
    QUALNAME ="types.ChatInviteAlready"

    def __init__ (self ,*,chat :"raw.base.Chat")->None :
        self .chat =chat 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChatInviteAlready":

        chat =TLObject .read (b )

        return ChatInviteAlready (chat =chat )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .chat .write ())

        return b .getvalue ()
