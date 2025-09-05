
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class StatsGraphError (TLObject ):
    """"""

    __slots__ :List [str ]=["error"]

    ID =0xbedc9822 
    QUALNAME ="types.StatsGraphError"

    def __init__ (self ,*,error :str )->None :
        self .error =error 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"StatsGraphError":

        error =String .read (b )

        return StatsGraphError (error =error )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .error ))

        return b .getvalue ()
