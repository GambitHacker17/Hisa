
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateReadChannelDiscussionOutbox (TLObject ):
    """"""

    __slots__ :List [str ]=["channel_id","top_msg_id","read_max_id"]

    ID =0x695c9e7c 
    QUALNAME ="types.UpdateReadChannelDiscussionOutbox"

    def __init__ (self ,*,channel_id :int ,top_msg_id :int ,read_max_id :int )->None :
        self .channel_id =channel_id 
        self .top_msg_id =top_msg_id 
        self .read_max_id =read_max_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateReadChannelDiscussionOutbox":

        channel_id =Long .read (b )

        top_msg_id =Int .read (b )

        read_max_id =Int .read (b )

        return UpdateReadChannelDiscussionOutbox (channel_id =channel_id ,top_msg_id =top_msg_id ,read_max_id =read_max_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .channel_id ))

        b .write (Int (self .top_msg_id ))

        b .write (Int (self .read_max_id ))

        return b .getvalue ()
