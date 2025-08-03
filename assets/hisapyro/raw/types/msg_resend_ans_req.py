
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MsgResendAnsReq (TLObject ):
    """"""

    __slots__ :List [str ]=["msg_ids"]

    ID =0x8610baeb 
    QUALNAME ="types.MsgResendAnsReq"

    def __init__ (self ,*,msg_ids :List [int ])->None :
        self .msg_ids =msg_ids 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MsgResendAnsReq":

        msg_ids =TLObject .read (b ,Long )

        return MsgResendAnsReq (msg_ids =msg_ids )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .msg_ids ,Long ))

        return b .getvalue ()
