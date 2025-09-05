
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AccountDaysTTL (TLObject ):
    """"""

    __slots__ :List [str ]=["days"]

    ID =0xb8d0afdf 
    QUALNAME ="types.AccountDaysTTL"

    def __init__ (self ,*,days :int )->None :
        self .days =days 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AccountDaysTTL":

        days =Int .read (b )

        return AccountDaysTTL (days =days )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .days ))

        return b .getvalue ()
