
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SentCodeTypeMissedCall (TLObject ):
    """"""

    __slots__ :List [str ]=["prefix","length"]

    ID =0x82006484 
    QUALNAME ="types.auth.SentCodeTypeMissedCall"

    def __init__ (self ,*,prefix :str ,length :int )->None :
        self .prefix =prefix 
        self .length =length 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SentCodeTypeMissedCall":

        prefix =String .read (b )

        length =Int .read (b )

        return SentCodeTypeMissedCall (prefix =prefix ,length =length )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .prefix ))

        b .write (Int (self .length ))

        return b .getvalue ()
