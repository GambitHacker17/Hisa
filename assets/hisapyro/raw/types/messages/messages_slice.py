
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessagesSlice (TLObject ):
    """"""

    __slots__ :List [str ]=["count","messages","chats","users","inexact","next_rate","offset_id_offset"]

    ID =0x3a54685e 
    QUALNAME ="types.messages.MessagesSlice"

    def __init__ (self ,*,count :int ,messages :List ["raw.base.Message"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"],inexact :Optional [bool ]=None ,next_rate :Optional [int ]=None ,offset_id_offset :Optional [int ]=None )->None :
        self .count =count 
        self .messages =messages 
        self .chats =chats 
        self .users =users 
        self .inexact =inexact 
        self .next_rate =next_rate 
        self .offset_id_offset =offset_id_offset 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessagesSlice":

        flags =Int .read (b )

        inexact =True if flags &(1 <<1 )else False 
        count =Int .read (b )

        next_rate =Int .read (b )if flags &(1 <<0 )else None 
        offset_id_offset =Int .read (b )if flags &(1 <<2 )else None 
        messages =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return MessagesSlice (count =count ,messages =messages ,chats =chats ,users =users ,inexact =inexact ,next_rate =next_rate ,offset_id_offset =offset_id_offset )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<1 )if self .inexact else 0 
        flags |=(1 <<0 )if self .next_rate is not None else 0 
        flags |=(1 <<2 )if self .offset_id_offset is not None else 0 
        b .write (Int (flags ))

        b .write (Int (self .count ))

        if self .next_rate is not None :
            b .write (Int (self .next_rate ))

        if self .offset_id_offset is not None :
            b .write (Int (self .offset_id_offset ))

        b .write (Vector (self .messages ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
