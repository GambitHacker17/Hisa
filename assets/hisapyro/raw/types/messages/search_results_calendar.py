
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SearchResultsCalendar (TLObject ):
    """"""

    __slots__ :List [str ]=["count","min_date","min_msg_id","periods","messages","chats","users","inexact","offset_id_offset"]

    ID =0x147ee23c 
    QUALNAME ="types.messages.SearchResultsCalendar"

    def __init__ (self ,*,count :int ,min_date :int ,min_msg_id :int ,periods :List ["raw.base.SearchResultsCalendarPeriod"],messages :List ["raw.base.Message"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"],inexact :Optional [bool ]=None ,offset_id_offset :Optional [int ]=None )->None :
        self .count =count 
        self .min_date =min_date 
        self .min_msg_id =min_msg_id 
        self .periods =periods 
        self .messages =messages 
        self .chats =chats 
        self .users =users 
        self .inexact =inexact 
        self .offset_id_offset =offset_id_offset 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SearchResultsCalendar":

        flags =Int .read (b )

        inexact =True if flags &(1 <<0 )else False 
        count =Int .read (b )

        min_date =Int .read (b )

        min_msg_id =Int .read (b )

        offset_id_offset =Int .read (b )if flags &(1 <<1 )else None 
        periods =TLObject .read (b )

        messages =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return SearchResultsCalendar (count =count ,min_date =min_date ,min_msg_id =min_msg_id ,periods =periods ,messages =messages ,chats =chats ,users =users ,inexact =inexact ,offset_id_offset =offset_id_offset )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .inexact else 0 
        flags |=(1 <<1 )if self .offset_id_offset is not None else 0 
        b .write (Int (flags ))

        b .write (Int (self .count ))

        b .write (Int (self .min_date ))

        b .write (Int (self .min_msg_id ))

        if self .offset_id_offset is not None :
            b .write (Int (self .offset_id_offset ))

        b .write (Vector (self .periods ))

        b .write (Vector (self .messages ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
