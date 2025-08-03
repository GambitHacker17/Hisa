
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class KeyboardButtonRow (TLObject ):
    """"""

    __slots__ :List [str ]=["buttons"]

    ID =0x77608b83 
    QUALNAME ="types.KeyboardButtonRow"

    def __init__ (self ,*,buttons :List ["raw.base.KeyboardButton"])->None :
        self .buttons =buttons 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"KeyboardButtonRow":

        buttons =TLObject .read (b )

        return KeyboardButtonRow (buttons =buttons )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .buttons ))

        return b .getvalue ()
