
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DiscardGroupCall (TLObject ):
    """"""

    __slots__ :List [str ]=["call"]

    ID =0x7a777135 
    QUALNAME ="functions.phone.DiscardGroupCall"

    def __init__ (self ,*,call :"raw.base.InputGroupCall")->None :
        self .call =call 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DiscardGroupCall":

        call =TLObject .read (b )

        return DiscardGroupCall (call =call )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .call .write ())

        return b .getvalue ()
