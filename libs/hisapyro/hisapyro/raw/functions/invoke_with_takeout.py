
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InvokeWithTakeout (TLObject ):
    """"""

    __slots__ :List [str ]=["takeout_id","query"]

    ID =0xaca9fd2e 
    QUALNAME ="functions.InvokeWithTakeout"

    def __init__ (self ,*,takeout_id :int ,query :TLObject )->None :
        self .takeout_id =takeout_id 
        self .query =query 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InvokeWithTakeout":

        takeout_id =Long .read (b )

        query =TLObject .read (b )

        return InvokeWithTakeout (takeout_id =takeout_id ,query =query )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .takeout_id ))

        b .write (self .query .write ())

        return b .getvalue ()
