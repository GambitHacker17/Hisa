
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateChannelAvailableMessages (TLObject ):
    """"""

    __slots__ :List [str ]=["channel_id","available_min_id"]

    ID =0xb23fc698 
    QUALNAME ="types.UpdateChannelAvailableMessages"

    def __init__ (self ,*,channel_id :int ,available_min_id :int )->None :
        self .channel_id =channel_id 
        self .available_min_id =available_min_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateChannelAvailableMessages":

        channel_id =Long .read (b )

        available_min_id =Int .read (b )

        return UpdateChannelAvailableMessages (channel_id =channel_id ,available_min_id =available_min_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .channel_id ))

        b .write (Int (self .available_min_id ))

        return b .getvalue ()
