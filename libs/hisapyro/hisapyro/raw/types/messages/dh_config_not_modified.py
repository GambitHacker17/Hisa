
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DhConfigNotModified (TLObject ):
    """"""

    __slots__ :List [str ]=["random"]

    ID =0xc0e24635 
    QUALNAME ="types.messages.DhConfigNotModified"

    def __init__ (self ,*,random :bytes )->None :
        self .random =random 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DhConfigNotModified":

        random =Bytes .read (b )

        return DhConfigNotModified (random =random )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Bytes (self .random ))

        return b .getvalue ()
