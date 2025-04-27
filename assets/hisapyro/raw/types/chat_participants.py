
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChatParticipants (TLObject ):
    """"""

    __slots__ :List [str ]=["chat_id","participants","version"]

    ID =0x3cbc93f8 
    QUALNAME ="types.ChatParticipants"

    def __init__ (self ,*,chat_id :int ,participants :List ["raw.base.ChatParticipant"],version :int )->None :
        self .chat_id =chat_id 
        self .participants =participants 
        self .version =version 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChatParticipants":

        chat_id =Long .read (b )

        participants =TLObject .read (b )

        version =Int .read (b )

        return ChatParticipants (chat_id =chat_id ,participants =participants ,version =version )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .chat_id ))

        b .write (Vector (self .participants ))

        b .write (Int (self .version ))

        return b .getvalue ()
