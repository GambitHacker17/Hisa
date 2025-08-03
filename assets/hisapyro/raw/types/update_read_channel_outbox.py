
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateReadChannelOutbox (TLObject ):
    """"""

    __slots__ :List [str ]=["channel_id","max_id"]

    ID =0xb75f99a9 
    QUALNAME ="types.UpdateReadChannelOutbox"

    def __init__ (self ,*,channel_id :int ,max_id :int )->None :
        self .channel_id =channel_id 
        self .max_id =max_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateReadChannelOutbox":

        channel_id =Long .read (b )

        max_id =Int .read (b )

        return UpdateReadChannelOutbox (channel_id =channel_id ,max_id =max_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .channel_id ))

        b .write (Int (self .max_id ))

        return b .getvalue ()
