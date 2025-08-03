
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageUserVote (TLObject ):
    """"""

    __slots__ :List [str ]=["user_id","option","date"]

    ID =0x34d247b4 
    QUALNAME ="types.MessageUserVote"

    def __init__ (self ,*,user_id :int ,option :bytes ,date :int )->None :
        self .user_id =user_id 
        self .option =option 
        self .date =date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageUserVote":

        user_id =Long .read (b )

        option =Bytes .read (b )

        date =Int .read (b )

        return MessageUserVote (user_id =user_id ,option =option ,date =date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .user_id ))

        b .write (Bytes (self .option ))

        b .write (Int (self .date ))

        return b .getvalue ()
