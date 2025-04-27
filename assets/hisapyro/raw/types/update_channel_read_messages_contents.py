
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateChannelReadMessagesContents (TLObject ):
    """"""

    __slots__ :List [str ]=["channel_id","messages","top_msg_id"]

    ID =0xea29055d 
    QUALNAME ="types.UpdateChannelReadMessagesContents"

    def __init__ (self ,*,channel_id :int ,messages :List [int ],top_msg_id :Optional [int ]=None )->None :
        self .channel_id =channel_id 
        self .messages =messages 
        self .top_msg_id =top_msg_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateChannelReadMessagesContents":

        flags =Int .read (b )

        channel_id =Long .read (b )

        top_msg_id =Int .read (b )if flags &(1 <<0 )else None 
        messages =TLObject .read (b ,Int )

        return UpdateChannelReadMessagesContents (channel_id =channel_id ,messages =messages ,top_msg_id =top_msg_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .top_msg_id is not None else 0 
        b .write (Int (flags ))

        b .write (Long (self .channel_id ))

        if self .top_msg_id is not None :
            b .write (Int (self .top_msg_id ))

        b .write (Vector (self .messages ,Int ))

        return b .getvalue ()
