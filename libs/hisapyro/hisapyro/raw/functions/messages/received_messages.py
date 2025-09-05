
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ReceivedMessages (TLObject ):
    """"""

    __slots__ :List [str ]=["max_id"]

    ID =0x5a954c0 
    QUALNAME ="functions.messages.ReceivedMessages"

    def __init__ (self ,*,max_id :int )->None :
        self .max_id =max_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ReceivedMessages":

        max_id =Int .read (b )

        return ReceivedMessages (max_id =max_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .max_id ))

        return b .getvalue ()
