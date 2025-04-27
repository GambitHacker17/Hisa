
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SentEmailCode (TLObject ):
    """"""

    __slots__ :List [str ]=["email_pattern","length"]

    ID =0x811f854f 
    QUALNAME ="types.account.SentEmailCode"

    def __init__ (self ,*,email_pattern :str ,length :int )->None :
        self .email_pattern =email_pattern 
        self .length =length 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SentEmailCode":

        email_pattern =String .read (b )

        length =Int .read (b )

        return SentEmailCode (email_pattern =email_pattern ,length =length )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .email_pattern ))

        b .write (Int (self .length ))

        return b .getvalue ()
