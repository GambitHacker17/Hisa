
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MsgNewDetailedInfo (TLObject ):
    """"""

    __slots__ :List [str ]=["answer_msg_id","bytes","status"]

    ID =0x809db6df 
    QUALNAME ="types.MsgNewDetailedInfo"

    def __init__ (self ,*,answer_msg_id :int ,bytes :int ,status :int )->None :
        self .answer_msg_id =answer_msg_id 
        self .bytes =bytes 
        self .status =status 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MsgNewDetailedInfo":

        answer_msg_id =Long .read (b )

        bytes =Int .read (b )

        status =Int .read (b )

        return MsgNewDetailedInfo (answer_msg_id =answer_msg_id ,bytes =bytes ,status =status )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .answer_msg_id ))

        b .write (Int (self .bytes ))

        b .write (Int (self .status ))

        return b .getvalue ()
