
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AffectedMessages (TLObject ):
    """"""

    __slots__ :List [str ]=["pts","pts_count"]

    ID =0x84d19185 
    QUALNAME ="types.messages.AffectedMessages"

    def __init__ (self ,*,pts :int ,pts_count :int )->None :
        self .pts =pts 
        self .pts_count =pts_count 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AffectedMessages":

        pts =Int .read (b )

        pts_count =Int .read (b )

        return AffectedMessages (pts =pts ,pts_count =pts_count )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .pts ))

        b .write (Int (self .pts_count ))

        return b .getvalue ()
