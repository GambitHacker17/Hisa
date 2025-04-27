
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AffectedHistory (TLObject ):
    """"""

    __slots__ :List [str ]=["pts","pts_count","offset"]

    ID =0xb45c69d1 
    QUALNAME ="types.messages.AffectedHistory"

    def __init__ (self ,*,pts :int ,pts_count :int ,offset :int )->None :
        self .pts =pts 
        self .pts_count =pts_count 
        self .offset =offset 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AffectedHistory":

        pts =Int .read (b )

        pts_count =Int .read (b )

        offset =Int .read (b )

        return AffectedHistory (pts =pts ,pts_count =pts_count ,offset =offset )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .pts ))

        b .write (Int (self .pts_count ))

        b .write (Int (self .offset ))

        return b .getvalue ()
