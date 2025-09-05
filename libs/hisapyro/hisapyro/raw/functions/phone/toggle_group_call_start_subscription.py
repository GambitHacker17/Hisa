
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ToggleGroupCallStartSubscription (TLObject ):
    """"""

    __slots__ :List [str ]=["call","subscribed"]

    ID =0x219c34e6 
    QUALNAME ="functions.phone.ToggleGroupCallStartSubscription"

    def __init__ (self ,*,call :"raw.base.InputGroupCall",subscribed :bool )->None :
        self .call =call 
        self .subscribed =subscribed 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ToggleGroupCallStartSubscription":

        call =TLObject .read (b )

        subscribed =Bool .read (b )

        return ToggleGroupCallStartSubscription (call =call ,subscribed =subscribed )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .call .write ())

        b .write (Bool (self .subscribed ))

        return b .getvalue ()
