
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateChatParticipantDelete (TLObject ):
    """"""

    __slots__ :List [str ]=["chat_id","user_id","version"]

    ID =0xe32f3d77 
    QUALNAME ="types.UpdateChatParticipantDelete"

    def __init__ (self ,*,chat_id :int ,user_id :int ,version :int )->None :
        self .chat_id =chat_id 
        self .user_id =user_id 
        self .version =version 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateChatParticipantDelete":

        chat_id =Long .read (b )

        user_id =Long .read (b )

        version =Int .read (b )

        return UpdateChatParticipantDelete (chat_id =chat_id ,user_id =user_id ,version =version )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .chat_id ))

        b .write (Long (self .user_id ))

        b .write (Int (self .version ))

        return b .getvalue ()
