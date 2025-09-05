
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class TranslateResult (TLObject ):
    """"""

    __slots__ :List [str ]=["result"]

    ID =0x33db32f8 
    QUALNAME ="types.messages.TranslateResult"

    def __init__ (self ,*,result :List ["raw.base.TextWithEntities"])->None :
        self .result =result 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"TranslateResult":

        result =TLObject .read (b )

        return TranslateResult (result =result )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .result ))

        return b .getvalue ()
