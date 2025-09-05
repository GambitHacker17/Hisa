
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageUserVoteMultiple (TLObject ):
    """"""

    __slots__ :List [str ]=["user_id","options","date"]

    ID =0x8a65e557 
    QUALNAME ="types.MessageUserVoteMultiple"

    def __init__ (self ,*,user_id :int ,options :List [bytes ],date :int )->None :
        self .user_id =user_id 
        self .options =options 
        self .date =date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageUserVoteMultiple":

        user_id =Long .read (b )

        options =TLObject .read (b ,Bytes )

        date =Int .read (b )

        return MessageUserVoteMultiple (user_id =user_id ,options =options ,date =date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .user_id ))

        b .write (Vector (self .options ,Bytes ))

        b .write (Int (self .date ))

        return b .getvalue ()
