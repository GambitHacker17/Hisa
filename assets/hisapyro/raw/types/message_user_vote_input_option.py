
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageUserVoteInputOption (TLObject ):
    """"""

    __slots__ :List [str ]=["user_id","date"]

    ID =0x3ca5b0ec 
    QUALNAME ="types.MessageUserVoteInputOption"

    def __init__ (self ,*,user_id :int ,date :int )->None :
        self .user_id =user_id 
        self .date =date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageUserVoteInputOption":

        user_id =Long .read (b )

        date =Int .read (b )

        return MessageUserVoteInputOption (user_id =user_id ,date =date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .user_id ))

        b .write (Int (self .date ))

        return b .getvalue ()
