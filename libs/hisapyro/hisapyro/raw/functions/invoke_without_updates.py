
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InvokeWithoutUpdates (TLObject ):
    """"""

    __slots__ :List [str ]=["query"]

    ID =0xbf9459b7 
    QUALNAME ="functions.InvokeWithoutUpdates"

    def __init__ (self ,*,query :TLObject )->None :
        self .query =query 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InvokeWithoutUpdates":

        query =TLObject .read (b )

        return InvokeWithoutUpdates (query =query )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .query .write ())

        return b .getvalue ()
