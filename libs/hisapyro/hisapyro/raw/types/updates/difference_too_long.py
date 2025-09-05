
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DifferenceTooLong (TLObject ):
    """"""

    __slots__ :List [str ]=["pts"]

    ID =0x4afe8f6d 
    QUALNAME ="types.updates.DifferenceTooLong"

    def __init__ (self ,*,pts :int )->None :
        self .pts =pts 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DifferenceTooLong":

        pts =Int .read (b )

        return DifferenceTooLong (pts =pts )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .pts ))

        return b .getvalue ()
