
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PhoneCallDiscardReasonBusy (TLObject ):
    """"""

    __slots__ :List [str ]=[]

    ID =0xfaf7e8c9 
    QUALNAME ="types.PhoneCallDiscardReasonBusy"

    def __init__ (self )->None :
        pass 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PhoneCallDiscardReasonBusy":

        return PhoneCallDiscardReasonBusy ()

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        return b .getvalue ()
