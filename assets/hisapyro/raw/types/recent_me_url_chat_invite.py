
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class RecentMeUrlChatInvite (TLObject ):
    """"""

    __slots__ :List [str ]=["url","chat_invite"]

    ID =0xeb49081d 
    QUALNAME ="types.RecentMeUrlChatInvite"

    def __init__ (self ,*,url :str ,chat_invite :"raw.base.ChatInvite")->None :
        self .url =url 
        self .chat_invite =chat_invite 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"RecentMeUrlChatInvite":

        url =String .read (b )

        chat_invite =TLObject .read (b )

        return RecentMeUrlChatInvite (url =url ,chat_invite =chat_invite )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .url ))

        b .write (self .chat_invite .write ())

        return b .getvalue ()
