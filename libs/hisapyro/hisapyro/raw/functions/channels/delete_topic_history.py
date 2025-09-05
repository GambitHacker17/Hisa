
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DeleteTopicHistory (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","top_msg_id"]

    ID =0x34435f2d 
    QUALNAME ="functions.channels.DeleteTopicHistory"

    def __init__ (self ,*,channel :"raw.base.InputChannel",top_msg_id :int )->None :
        self .channel =channel 
        self .top_msg_id =top_msg_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DeleteTopicHistory":

        channel =TLObject .read (b )

        top_msg_id =Int .read (b )

        return DeleteTopicHistory (channel =channel ,top_msg_id =top_msg_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .channel .write ())

        b .write (Int (self .top_msg_id ))

        return b .getvalue ()
