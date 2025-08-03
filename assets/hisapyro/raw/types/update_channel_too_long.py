
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateChannelTooLong (TLObject ):
    """"""

    __slots__ :List [str ]=["channel_id","pts"]

    ID =0x108d941f 
    QUALNAME ="types.UpdateChannelTooLong"

    def __init__ (self ,*,channel_id :int ,pts :Optional [int ]=None )->None :
        self .channel_id =channel_id 
        self .pts =pts 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateChannelTooLong":

        flags =Int .read (b )

        channel_id =Long .read (b )

        pts =Int .read (b )if flags &(1 <<0 )else None 
        return UpdateChannelTooLong (channel_id =channel_id ,pts =pts )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .pts is not None else 0 
        b .write (Int (flags ))

        b .write (Long (self .channel_id ))

        if self .pts is not None :
            b .write (Int (self .pts ))

        return b .getvalue ()
