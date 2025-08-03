
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateMessagePollVote (TLObject ):
    """"""

    __slots__ :List [str ]=["poll_id","user_id","options","qts"]

    ID =0x106395c9 
    QUALNAME ="types.UpdateMessagePollVote"

    def __init__ (self ,*,poll_id :int ,user_id :int ,options :List [bytes ],qts :int )->None :
        self .poll_id =poll_id 
        self .user_id =user_id 
        self .options =options 
        self .qts =qts 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateMessagePollVote":

        poll_id =Long .read (b )

        user_id =Long .read (b )

        options =TLObject .read (b ,Bytes )

        qts =Int .read (b )

        return UpdateMessagePollVote (poll_id =poll_id ,user_id =user_id ,options =options ,qts =qts )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .poll_id ))

        b .write (Long (self .user_id ))

        b .write (Vector (self .options ,Bytes ))

        b .write (Int (self .qts ))

        return b .getvalue ()
