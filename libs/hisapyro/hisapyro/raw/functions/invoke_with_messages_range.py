
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InvokeWithMessagesRange (TLObject ):
    """"""

    __slots__ :List [str ]=["range","query"]

    ID =0x365275f2 
    QUALNAME ="functions.InvokeWithMessagesRange"

    def __init__ (self ,*,range :"raw.base.MessageRange",query :TLObject )->None :
        self .range =range 
        self .query =query 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InvokeWithMessagesRange":

        range =TLObject .read (b )

        query =TLObject .read (b )

        return InvokeWithMessagesRange (range =range ,query =query )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .range .write ())

        b .write (self .query .write ())

        return b .getvalue ()
