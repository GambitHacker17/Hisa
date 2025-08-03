
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageReactionsList (TLObject ):
    """"""

    __slots__ :List [str ]=["count","reactions","chats","users","next_offset"]

    ID =0x31bd492d 
    QUALNAME ="types.messages.MessageReactionsList"

    def __init__ (self ,*,count :int ,reactions :List ["raw.base.MessagePeerReaction"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"],next_offset :Optional [str ]=None )->None :
        self .count =count 
        self .reactions =reactions 
        self .chats =chats 
        self .users =users 
        self .next_offset =next_offset 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageReactionsList":

        flags =Int .read (b )

        count =Int .read (b )

        reactions =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        next_offset =String .read (b )if flags &(1 <<0 )else None 
        return MessageReactionsList (count =count ,reactions =reactions ,chats =chats ,users =users ,next_offset =next_offset )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .next_offset is not None else 0 
        b .write (Int (flags ))

        b .write (Int (self .count ))

        b .write (Vector (self .reactions ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        if self .next_offset is not None :
            b .write (String (self .next_offset ))

        return b .getvalue ()
