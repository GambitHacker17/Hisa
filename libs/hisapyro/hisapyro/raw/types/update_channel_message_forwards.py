
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateChannelMessageForwards (TLObject ):
    """"""

    __slots__ :List [str ]=["channel_id","id","forwards"]

    ID =0xd29a27f4 
    QUALNAME ="types.UpdateChannelMessageForwards"

    def __init__ (self ,*,channel_id :int ,id :int ,forwards :int )->None :
        self .channel_id =channel_id 
        self .id =id 
        self .forwards =forwards 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateChannelMessageForwards":

        channel_id =Long .read (b )

        id =Int .read (b )

        forwards =Int .read (b )

        return UpdateChannelMessageForwards (channel_id =channel_id ,id =id ,forwards =forwards )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .channel_id ))

        b .write (Int (self .id ))

        b .write (Int (self .forwards ))

        return b .getvalue ()
