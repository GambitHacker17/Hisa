
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ReceivedQueue (TLObject ):
    """"""

    __slots__ :List [str ]=["max_qts"]

    ID =0x55a5bb66 
    QUALNAME ="functions.messages.ReceivedQueue"

    def __init__ (self ,*,max_qts :int )->None :
        self .max_qts =max_qts 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ReceivedQueue":

        max_qts =Int .read (b )

        return ReceivedQueue (max_qts =max_qts )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .max_qts ))

        return b .getvalue ()
