
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class StatsPercentValue (TLObject ):
    """"""

    __slots__ :List [str ]=["part","total"]

    ID =0xcbce2fe0 
    QUALNAME ="types.StatsPercentValue"

    def __init__ (self ,*,part :float ,total :float )->None :
        self .part =part 
        self .total =total 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"StatsPercentValue":

        part =Double .read (b )

        total =Double .read (b )

        return StatsPercentValue (part =part ,total =total )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Double (self .part ))

        b .write (Double (self .total ))

        return b .getvalue ()
