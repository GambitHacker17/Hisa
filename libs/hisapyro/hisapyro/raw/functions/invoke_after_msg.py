
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InvokeAfterMsg (TLObject ):
    """"""

    __slots__ :List [str ]=["msg_id","query"]

    ID =0xcb9f372d 
    QUALNAME ="functions.InvokeAfterMsg"

    def __init__ (self ,*,msg_id :int ,query :TLObject )->None :
        self .msg_id =msg_id 
        self .query =query 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InvokeAfterMsg":

        msg_id =Long .read (b )

        query =TLObject .read (b )

        return InvokeAfterMsg (msg_id =msg_id ,query =query )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .msg_id ))

        b .write (self .query .write ())

        return b .getvalue ()
