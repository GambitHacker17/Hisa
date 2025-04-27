
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelParticipant (TLObject ):
    """"""

    __slots__ :List [str ]=["participant","chats","users"]

    ID =0xdfb80317 
    QUALNAME ="types.channels.ChannelParticipant"

    def __init__ (self ,*,participant :"raw.base.ChannelParticipant",chats :List ["raw.base.Chat"],users :List ["raw.base.User"])->None :
        self .participant =participant 
        self .chats =chats 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelParticipant":

        participant =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return ChannelParticipant (participant =participant ,chats =chats ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .participant .write ())

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
