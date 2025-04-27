
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class StatsGraphAsync (TLObject ):
    """"""

    __slots__ :List [str ]=["token"]

    ID =0x4a27eb2d 
    QUALNAME ="types.StatsGraphAsync"

    def __init__ (self ,*,token :str )->None :
        self .token =token 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"StatsGraphAsync":

        token =String .read (b )

        return StatsGraphAsync (token =token )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .token ))

        return b .getvalue ()
