
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateChannelPinnedTopic (TLObject ):
    """"""

    __slots__ :List [str ]=["channel_id","topic_id","pinned"]

    ID =0x192efbe3 
    QUALNAME ="types.UpdateChannelPinnedTopic"

    def __init__ (self ,*,channel_id :int ,topic_id :int ,pinned :Optional [bool ]=None )->None :
        self .channel_id =channel_id 
        self .topic_id =topic_id 
        self .pinned =pinned 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateChannelPinnedTopic":

        flags =Int .read (b )

        pinned =True if flags &(1 <<0 )else False 
        channel_id =Long .read (b )

        topic_id =Int .read (b )

        return UpdateChannelPinnedTopic (channel_id =channel_id ,topic_id =topic_id ,pinned =pinned )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .pinned else 0 
        b .write (Int (flags ))

        b .write (Long (self .channel_id ))

        b .write (Int (self .topic_id ))

        return b .getvalue ()
