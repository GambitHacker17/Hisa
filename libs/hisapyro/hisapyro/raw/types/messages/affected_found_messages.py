
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AffectedFoundMessages (TLObject ):
    """"""

    __slots__ :List [str ]=["pts","pts_count","offset","messages"]

    ID =0xef8d3e6c 
    QUALNAME ="types.messages.AffectedFoundMessages"

    def __init__ (self ,*,pts :int ,pts_count :int ,offset :int ,messages :List [int ])->None :
        self .pts =pts 
        self .pts_count =pts_count 
        self .offset =offset 
        self .messages =messages 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AffectedFoundMessages":

        pts =Int .read (b )

        pts_count =Int .read (b )

        offset =Int .read (b )

        messages =TLObject .read (b ,Int )

        return AffectedFoundMessages (pts =pts ,pts_count =pts_count ,offset =offset ,messages =messages )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .pts ))

        b .write (Int (self .pts_count ))

        b .write (Int (self .offset ))

        b .write (Vector (self .messages ,Int ))

        return b .getvalue ()
