
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageActionChatJoinedByLink (TLObject ):
    """"""

    __slots__ :List [str ]=["inviter_id"]

    ID =0x31224c3 
    QUALNAME ="types.MessageActionChatJoinedByLink"

    def __init__ (self ,*,inviter_id :int )->None :
        self .inviter_id =inviter_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageActionChatJoinedByLink":

        inviter_id =Long .read (b )

        return MessageActionChatJoinedByLink (inviter_id =inviter_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .inviter_id ))

        return b .getvalue ()
