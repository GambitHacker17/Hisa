
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AdminLogResults (TLObject ):
    """"""

    __slots__ :List [str ]=["events","chats","users"]

    ID =0xed8af74d 
    QUALNAME ="types.channels.AdminLogResults"

    def __init__ (self ,*,events :List ["raw.base.ChannelAdminLogEvent"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"])->None :
        self .events =events 
        self .chats =chats 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AdminLogResults":

        events =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return AdminLogResults (events =events ,chats =chats ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .events ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
