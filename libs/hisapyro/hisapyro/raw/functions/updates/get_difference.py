
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetDifference (TLObject ):
    """"""

    __slots__ :List [str ]=["pts","date","qts","pts_total_limit"]

    ID =0x25939651 
    QUALNAME ="functions.updates.GetDifference"

    def __init__ (self ,*,pts :int ,date :int ,qts :int ,pts_total_limit :Optional [int ]=None )->None :
        self .pts =pts 
        self .date =date 
        self .qts =qts 
        self .pts_total_limit =pts_total_limit 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetDifference":

        flags =Int .read (b )

        pts =Int .read (b )

        pts_total_limit =Int .read (b )if flags &(1 <<0 )else None 
        date =Int .read (b )

        qts =Int .read (b )

        return GetDifference (pts =pts ,date =date ,qts =qts ,pts_total_limit =pts_total_limit )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .pts_total_limit is not None else 0 
        b .write (Int (flags ))

        b .write (Int (self .pts ))

        if self .pts_total_limit is not None :
            b .write (Int (self .pts_total_limit ))

        b .write (Int (self .date ))

        b .write (Int (self .qts ))

        return b .getvalue ()
