
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InvokeAfterMsgs (TLObject ):
    """"""

    __slots__ :List [str ]=["msg_ids","query"]

    ID =0x3dc4b4f0 
    QUALNAME ="functions.InvokeAfterMsgs"

    def __init__ (self ,*,msg_ids :List [int ],query :TLObject )->None :
        self .msg_ids =msg_ids 
        self .query =query 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InvokeAfterMsgs":

        msg_ids =TLObject .read (b ,Long )

        query =TLObject .read (b )

        return InvokeAfterMsgs (msg_ids =msg_ids ,query =query )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .msg_ids ,Long ))

        b .write (self .query .write ())

        return b .getvalue ()
