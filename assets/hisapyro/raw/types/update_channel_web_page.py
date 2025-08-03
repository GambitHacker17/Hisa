
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateChannelWebPage (TLObject ):
    """"""

    __slots__ :List [str ]=["channel_id","webpage","pts","pts_count"]

    ID =0x2f2ba99f 
    QUALNAME ="types.UpdateChannelWebPage"

    def __init__ (self ,*,channel_id :int ,webpage :"raw.base.WebPage",pts :int ,pts_count :int )->None :
        self .channel_id =channel_id 
        self .webpage =webpage 
        self .pts =pts 
        self .pts_count =pts_count 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateChannelWebPage":

        channel_id =Long .read (b )

        webpage =TLObject .read (b )

        pts =Int .read (b )

        pts_count =Int .read (b )

        return UpdateChannelWebPage (channel_id =channel_id ,webpage =webpage ,pts =pts ,pts_count =pts_count )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .channel_id ))

        b .write (self .webpage .write ())

        b .write (Int (self .pts ))

        b .write (Int (self .pts_count ))

        return b .getvalue ()
