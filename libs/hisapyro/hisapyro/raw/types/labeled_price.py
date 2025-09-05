
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class LabeledPrice (TLObject ):
    """"""

    __slots__ :List [str ]=["label","amount"]

    ID =0xcb296bf8 
    QUALNAME ="types.LabeledPrice"

    def __init__ (self ,*,label :str ,amount :int )->None :
        self .label =label 
        self .amount =amount 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"LabeledPrice":

        label =String .read (b )

        amount =Long .read (b )

        return LabeledPrice (label =label ,amount =amount )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .label ))

        b .write (Long (self .amount ))

        return b .getvalue ()
