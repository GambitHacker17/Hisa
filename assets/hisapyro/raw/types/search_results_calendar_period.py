
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SearchResultsCalendarPeriod (TLObject ):
    """"""

    __slots__ :List [str ]=["date","min_msg_id","max_msg_id","count"]

    ID =0xc9b0539f 
    QUALNAME ="types.SearchResultsCalendarPeriod"

    def __init__ (self ,*,date :int ,min_msg_id :int ,max_msg_id :int ,count :int )->None :
        self .date =date 
        self .min_msg_id =min_msg_id 
        self .max_msg_id =max_msg_id 
        self .count =count 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SearchResultsCalendarPeriod":

        date =Int .read (b )

        min_msg_id =Int .read (b )

        max_msg_id =Int .read (b )

        count =Int .read (b )

        return SearchResultsCalendarPeriod (date =date ,min_msg_id =min_msg_id ,max_msg_id =max_msg_id ,count =count )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .date ))

        b .write (Int (self .min_msg_id ))

        b .write (Int (self .max_msg_id ))

        b .write (Int (self .count ))

        return b .getvalue ()
