
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ImportLoginToken (TLObject ):
    """"""

    __slots__ :List [str ]=["token"]

    ID =0x95ac5ce4 
    QUALNAME ="functions.auth.ImportLoginToken"

    def __init__ (self ,*,token :bytes )->None :
        self .token =token 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ImportLoginToken":

        token =Bytes .read (b )

        return ImportLoginToken (token =token )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Bytes (self .token ))

        return b .getvalue ()
