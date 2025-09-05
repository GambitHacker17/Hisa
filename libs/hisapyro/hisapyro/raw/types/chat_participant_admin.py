
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChatParticipantAdmin (TLObject ):
    """"""

    __slots__ :List [str ]=["user_id","inviter_id","date"]

    ID =0xa0933f5b 
    QUALNAME ="types.ChatParticipantAdmin"

    def __init__ (self ,*,user_id :int ,inviter_id :int ,date :int )->None :
        self .user_id =user_id 
        self .inviter_id =inviter_id 
        self .date =date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChatParticipantAdmin":

        user_id =Long .read (b )

        inviter_id =Long .read (b )

        date =Int .read (b )

        return ChatParticipantAdmin (user_id =user_id ,inviter_id =inviter_id ,date =date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .user_id ))

        b .write (Long (self .inviter_id ))

        b .write (Int (self .date ))

        return b .getvalue ()
