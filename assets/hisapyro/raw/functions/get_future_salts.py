
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetFutureSalts (TLObject ):
    """"""

    __slots__ :List [str ]=["num"]

    ID =0xb921bd04 
    QUALNAME ="functions.GetFutureSalts"

    def __init__ (self ,*,num :int )->None :
        self .num =num 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetFutureSalts":

        num =Int .read (b )

        return GetFutureSalts (num =num )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .num ))

        return b .getvalue ()
