
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SponsoredMessages (TLObject ):
    """"""

    __slots__ :List [str ]=["messages","chats","users","posts_between"]

    ID =0xc9ee1d87 
    QUALNAME ="types.messages.SponsoredMessages"

    def __init__ (self ,*,messages :List ["raw.base.SponsoredMessage"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"],posts_between :Optional [int ]=None )->None :
        self .messages =messages 
        self .chats =chats 
        self .users =users 
        self .posts_between =posts_between 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SponsoredMessages":

        flags =Int .read (b )

        posts_between =Int .read (b )if flags &(1 <<0 )else None 
        messages =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return SponsoredMessages (messages =messages ,chats =chats ,users =users ,posts_between =posts_between )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .posts_between is not None else 0 
        b .write (Int (flags ))

        if self .posts_between is not None :
            b .write (Int (self .posts_between ))

        b .write (Vector (self .messages ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
