
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateDeleteMessages (TLObject ):
    """"""

    __slots__ :List [str ]=["messages","pts","pts_count"]

    ID =0xa20db0e5 
    QUALNAME ="types.UpdateDeleteMessages"

    def __init__ (self ,*,messages :List [int ],pts :int ,pts_count :int )->None :
        self .messages =messages 
        self .pts =pts 
        self .pts_count =pts_count 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateDeleteMessages":

        messages =TLObject .read (b ,Int )

        pts =Int .read (b )

        pts_count =Int .read (b )

        return UpdateDeleteMessages (messages =messages ,pts =pts ,pts_count =pts_count )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .messages ,Int ))

        b .write (Int (self .pts ))

        b .write (Int (self .pts_count ))

        return b .getvalue ()
