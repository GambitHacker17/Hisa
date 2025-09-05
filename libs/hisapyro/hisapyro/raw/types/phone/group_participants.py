
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GroupParticipants (TLObject ):
    """"""

    __slots__ :List [str ]=["count","participants","next_offset","chats","users","version"]

    ID =0xf47751b6 
    QUALNAME ="types.phone.GroupParticipants"

    def __init__ (self ,*,count :int ,participants :List ["raw.base.GroupCallParticipant"],next_offset :str ,chats :List ["raw.base.Chat"],users :List ["raw.base.User"],version :int )->None :
        self .count =count 
        self .participants =participants 
        self .next_offset =next_offset 
        self .chats =chats 
        self .users =users 
        self .version =version 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GroupParticipants":

        count =Int .read (b )

        participants =TLObject .read (b )

        next_offset =String .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        version =Int .read (b )

        return GroupParticipants (count =count ,participants =participants ,next_offset =next_offset ,chats =chats ,users =users ,version =version )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .count ))

        b .write (Vector (self .participants ))

        b .write (String (self .next_offset ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        b .write (Int (self .version ))

        return b .getvalue ()
