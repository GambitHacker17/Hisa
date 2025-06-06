
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SendMessageUploadRoundAction (TLObject ):
    """"""

    __slots__ :List [str ]=["progress"]

    ID =0x243e1c66 
    QUALNAME ="types.SendMessageUploadRoundAction"

    def __init__ (self ,*,progress :int )->None :
        self .progress =progress 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SendMessageUploadRoundAction":

        progress =Int .read (b )

        return SendMessageUploadRoundAction (progress =progress )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .progress ))

        return b .getvalue ()
