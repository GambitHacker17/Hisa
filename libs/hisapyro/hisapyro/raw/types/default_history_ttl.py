
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DefaultHistoryTTL (TLObject ):
    """"""

    __slots__ :List [str ]=["period"]

    ID =0x43b46b20 
    QUALNAME ="types.DefaultHistoryTTL"

    def __init__ (self ,*,period :int )->None :
        self .period =period 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DefaultHistoryTTL":

        period =Int .read (b )

        return DefaultHistoryTTL (period =period )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .period ))

        return b .getvalue ()
