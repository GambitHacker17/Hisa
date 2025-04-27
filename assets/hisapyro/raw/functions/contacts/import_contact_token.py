
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ImportContactToken (TLObject ):
    """"""

    __slots__ :List [str ]=["token"]

    ID =0x13005788 
    QUALNAME ="functions.contacts.ImportContactToken"

    def __init__ (self ,*,token :str )->None :
        self .token =token 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ImportContactToken":

        token =String .read (b )

        return ImportContactToken (token =token )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .token ))

        return b .getvalue ()
