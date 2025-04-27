
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PeerSettings (TLObject ):
    """"""

    __slots__ :List [str ]=["settings","chats","users"]

    ID =0x6880b94d 
    QUALNAME ="types.messages.PeerSettings"

    def __init__ (self ,*,settings :"raw.base.PeerSettings",chats :List ["raw.base.Chat"],users :List ["raw.base.User"])->None :
        self .settings =settings 
        self .chats =chats 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PeerSettings":

        settings =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return PeerSettings (settings =settings ,chats =chats ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .settings .write ())

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
