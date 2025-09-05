
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ReqPqMulti (TLObject ):
    """"""

    __slots__ :List [str ]=["nonce"]

    ID =0xbe7e8ef1 
    QUALNAME ="functions.ReqPqMulti"

    def __init__ (self ,*,nonce :int )->None :
        self .nonce =nonce 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ReqPqMulti":

        nonce =Int128 .read (b )

        return ReqPqMulti (nonce =nonce )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int128 (self .nonce ))

        return b .getvalue ()
