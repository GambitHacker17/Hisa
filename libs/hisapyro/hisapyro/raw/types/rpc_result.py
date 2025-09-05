
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class RpcResult (TLObject ):
    """"""

    __slots__ :List [str ]=["req_msg_id","result"]

    ID =0xf35c6d01 
    QUALNAME ="types.RpcResult"

    def __init__ (self ,*,req_msg_id :int ,result :TLObject )->None :
        self .req_msg_id =req_msg_id 
        self .result =result 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"RpcResult":

        req_msg_id =Long .read (b )

        result =TLObject .read (b )

        return RpcResult (req_msg_id =req_msg_id ,result =result )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .req_msg_id ))

        b .write (self .result .write ())

        return b .getvalue ()
