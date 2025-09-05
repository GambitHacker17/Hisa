
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateDeleteChannelMessages (TLObject ):
    """"""

    __slots__ :List [str ]=["channel_id","messages","pts","pts_count"]

    ID =0xc32d5b12 
    QUALNAME ="types.UpdateDeleteChannelMessages"

    def __init__ (self ,*,channel_id :int ,messages :List [int ],pts :int ,pts_count :int )->None :
        self .channel_id =channel_id 
        self .messages =messages 
        self .pts =pts 
        self .pts_count =pts_count 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateDeleteChannelMessages":

        channel_id =Long .read (b )

        messages =TLObject .read (b ,Int )

        pts =Int .read (b )

        pts_count =Int .read (b )

        return UpdateDeleteChannelMessages (channel_id =channel_id ,messages =messages ,pts =pts ,pts_count =pts_count )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .channel_id ))

        b .write (Vector (self .messages ,Int ))

        b .write (Int (self .pts ))

        b .write (Int (self .pts_count ))

        return b .getvalue ()
