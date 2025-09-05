
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageEntityMentionName (TLObject ):
    """"""

    __slots__ :List [str ]=["offset","length","user_id"]

    ID =0xdc7b1140 
    QUALNAME ="types.MessageEntityMentionName"

    def __init__ (self ,*,offset :int ,length :int ,user_id :int )->None :
        self .offset =offset 
        self .length =length 
        self .user_id =user_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageEntityMentionName":

        offset =Int .read (b )

        length =Int .read (b )

        user_id =Long .read (b )

        return MessageEntityMentionName (offset =offset ,length =length ,user_id =user_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .offset ))

        b .write (Int (self .length ))

        b .write (Long (self .user_id ))

        return b .getvalue ()
