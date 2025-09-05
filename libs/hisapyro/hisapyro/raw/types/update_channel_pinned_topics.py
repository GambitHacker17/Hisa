
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateChannelPinnedTopics (TLObject ):
    """"""

    __slots__ :List [str ]=["channel_id","order"]

    ID =0xfe198602 
    QUALNAME ="types.UpdateChannelPinnedTopics"

    def __init__ (self ,*,channel_id :int ,order :Optional [List [int ]]=None )->None :
        self .channel_id =channel_id 
        self .order =order 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateChannelPinnedTopics":

        flags =Int .read (b )

        channel_id =Long .read (b )

        order =TLObject .read (b ,Int )if flags &(1 <<0 )else []

        return UpdateChannelPinnedTopics (channel_id =channel_id ,order =order )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .order else 0 
        b .write (Int (flags ))

        b .write (Long (self .channel_id ))

        if self .order is not None :
            b .write (Vector (self .order ,Int ))

        return b .getvalue ()
