
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DifferenceEmpty (TLObject ):
    """"""

    __slots__ :List [str ]=["date","seq"]

    ID =0x5d75a138 
    QUALNAME ="types.updates.DifferenceEmpty"

    def __init__ (self ,*,date :int ,seq :int )->None :
        self .date =date 
        self .seq =seq 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DifferenceEmpty":

        date =Int .read (b )

        seq =Int .read (b )

        return DifferenceEmpty (date =date ,seq =seq )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .date ))

        b .write (Int (self .seq ))

        return b .getvalue ()
