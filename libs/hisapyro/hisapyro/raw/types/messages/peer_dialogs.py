
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PeerDialogs (TLObject ):
    """"""

    __slots__ :List [str ]=["dialogs","messages","chats","users","state"]

    ID =0x3371c354 
    QUALNAME ="types.messages.PeerDialogs"

    def __init__ (self ,*,dialogs :List ["raw.base.Dialog"],messages :List ["raw.base.Message"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"],state :"raw.base.updates.State")->None :
        self .dialogs =dialogs 
        self .messages =messages 
        self .chats =chats 
        self .users =users 
        self .state =state 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PeerDialogs":

        dialogs =TLObject .read (b )

        messages =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        state =TLObject .read (b )

        return PeerDialogs (dialogs =dialogs ,messages =messages ,chats =chats ,users =users ,state =state )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .dialogs ))

        b .write (Vector (self .messages ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        b .write (self .state .write ())

        return b .getvalue ()
