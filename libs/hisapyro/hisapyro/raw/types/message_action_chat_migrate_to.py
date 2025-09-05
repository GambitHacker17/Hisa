
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageActionChatMigrateTo (TLObject ):
    """"""

    __slots__ :List [str ]=["channel_id"]

    ID =0xe1037f92 
    QUALNAME ="types.MessageActionChatMigrateTo"

    def __init__ (self ,*,channel_id :int )->None :
        self .channel_id =channel_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageActionChatMigrateTo":

        channel_id =Long .read (b )

        return MessageActionChatMigrateTo (channel_id =channel_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .channel_id ))

        return b .getvalue ()
