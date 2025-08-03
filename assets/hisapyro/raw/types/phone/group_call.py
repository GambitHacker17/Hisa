
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GroupCall (TLObject ):
    """"""

    __slots__ :List [str ]=["call","participants","participants_next_offset","chats","users"]

    ID =0x9e727aad 
    QUALNAME ="types.phone.GroupCall"

    def __init__ (self ,*,call :"raw.base.GroupCall",participants :List ["raw.base.GroupCallParticipant"],participants_next_offset :str ,chats :List ["raw.base.Chat"],users :List ["raw.base.User"])->None :
        self .call =call 
        self .participants =participants 
        self .participants_next_offset =participants_next_offset 
        self .chats =chats 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GroupCall":

        call =TLObject .read (b )

        participants =TLObject .read (b )

        participants_next_offset =String .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return GroupCall (call =call ,participants =participants ,participants_next_offset =participants_next_offset ,chats =chats ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .call .write ())

        b .write (Vector (self .participants ))

        b .write (String (self .participants_next_offset ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
