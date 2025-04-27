
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class StatsDateRangeDays (TLObject ):
    """"""

    __slots__ :List [str ]=["min_date","max_date"]

    ID =0xb637edaf 
    QUALNAME ="types.StatsDateRangeDays"

    def __init__ (self ,*,min_date :int ,max_date :int )->None :
        self .min_date =min_date 
        self .max_date =max_date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"StatsDateRangeDays":

        min_date =Int .read (b )

        max_date =Int .read (b )

        return StatsDateRangeDays (min_date =min_date ,max_date =max_date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .min_date ))

        b .write (Int (self .max_date ))

        return b .getvalue ()
