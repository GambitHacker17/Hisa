
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class TextConcat (TLObject ):
    """"""

    __slots__ :List [str ]=["texts"]

    ID =0x7e6260d7 
    QUALNAME ="types.TextConcat"

    def __init__ (self ,*,texts :List ["raw.base.RichText"])->None :
        self .texts =texts 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"TextConcat":

        texts =TLObject .read (b )

        return TextConcat (texts =texts )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .texts ))

        return b .getvalue ()
