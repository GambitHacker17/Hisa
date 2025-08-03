
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class RecentMeUrls (TLObject ):
    """"""

    __slots__ :List [str ]=["urls","chats","users"]

    ID =0xe0310d7 
    QUALNAME ="types.help.RecentMeUrls"

    def __init__ (self ,*,urls :List ["raw.base.RecentMeUrl"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"])->None :
        self .urls =urls 
        self .chats =chats 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"RecentMeUrls":

        urls =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return RecentMeUrls (urls =urls ,chats =chats ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .urls ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
