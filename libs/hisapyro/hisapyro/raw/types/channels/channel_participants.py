
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelParticipants (TLObject ):
    """"""

    __slots__ :List [str ]=["count","participants","chats","users"]

    ID =0x9ab0feaf 
    QUALNAME ="types.channels.ChannelParticipants"

    def __init__ (self ,*,count :int ,participants :List ["raw.base.ChannelParticipant"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"])->None :
        self .count =count 
        self .participants =participants 
        self .chats =chats 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelParticipants":

        count =Int .read (b )

        participants =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return ChannelParticipants (count =count ,participants =participants ,chats =chats ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .count ))

        b .write (Vector (self .participants ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
