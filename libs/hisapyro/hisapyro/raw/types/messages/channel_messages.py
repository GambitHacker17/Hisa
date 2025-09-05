
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelMessages (TLObject ):
    """"""

    __slots__ :List [str ]=["pts","count","messages","topics","chats","users","inexact","offset_id_offset"]

    ID =0xc776ba4e 
    QUALNAME ="types.messages.ChannelMessages"

    def __init__ (self ,*,pts :int ,count :int ,messages :List ["raw.base.Message"],topics :List ["raw.base.ForumTopic"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"],inexact :Optional [bool ]=None ,offset_id_offset :Optional [int ]=None )->None :
        self .pts =pts 
        self .count =count 
        self .messages =messages 
        self .topics =topics 
        self .chats =chats 
        self .users =users 
        self .inexact =inexact 
        self .offset_id_offset =offset_id_offset 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelMessages":

        flags =Int .read (b )

        inexact =True if flags &(1 <<1 )else False 
        pts =Int .read (b )

        count =Int .read (b )

        offset_id_offset =Int .read (b )if flags &(1 <<2 )else None 
        messages =TLObject .read (b )

        topics =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return ChannelMessages (pts =pts ,count =count ,messages =messages ,topics =topics ,chats =chats ,users =users ,inexact =inexact ,offset_id_offset =offset_id_offset )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<1 )if self .inexact else 0 
        flags |=(1 <<2 )if self .offset_id_offset is not None else 0 
        b .write (Int (flags ))

        b .write (Int (self .pts ))

        b .write (Int (self .count ))

        if self .offset_id_offset is not None :
            b .write (Int (self .offset_id_offset ))

        b .write (Vector (self .messages ))

        b .write (Vector (self .topics ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
