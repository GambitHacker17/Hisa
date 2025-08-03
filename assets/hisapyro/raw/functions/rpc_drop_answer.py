
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class RpcDropAnswer (TLObject ):
    """"""

    __slots__ :List [str ]=["req_msg_id"]

    ID =0x58e4a740 
    QUALNAME ="functions.RpcDropAnswer"

    def __init__ (self ,*,req_msg_id :int )->None :
        self .req_msg_id =req_msg_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"RpcDropAnswer":

        req_msg_id =Long .read (b )

        return RpcDropAnswer (req_msg_id =req_msg_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .req_msg_id ))

        return b .getvalue ()
