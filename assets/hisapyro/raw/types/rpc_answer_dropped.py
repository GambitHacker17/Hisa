
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class RpcAnswerDropped (TLObject ):
    """"""

    __slots__ :List [str ]=["msg_id","seq_no","bytes"]

    ID =0xa43ad8b7 
    QUALNAME ="types.RpcAnswerDropped"

    def __init__ (self ,*,msg_id :int ,seq_no :int ,bytes :int )->None :
        self .msg_id =msg_id 
        self .seq_no =seq_no 
        self .bytes =bytes 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"RpcAnswerDropped":

        msg_id =Long .read (b )

        seq_no =Int .read (b )

        bytes =Int .read (b )

        return RpcAnswerDropped (msg_id =msg_id ,seq_no =seq_no ,bytes =bytes )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .msg_id ))

        b .write (Int (self .seq_no ))

        b .write (Int (self .bytes ))

        return b .getvalue ()
