
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SentCodeTypeSms (TLObject ):
    """"""

    __slots__ :List [str ]=["length"]

    ID =0xc000bba2 
    QUALNAME ="types.auth.SentCodeTypeSms"

    def __init__ (self ,*,length :int )->None :
        self .length =length 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SentCodeTypeSms":

        length =Int .read (b )

        return SentCodeTypeSms (length =length )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .length ))

        return b .getvalue ()
