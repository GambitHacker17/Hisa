
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ToggleNoForwards (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","enabled"]

    ID =0xb11eafa2 
    QUALNAME ="functions.messages.ToggleNoForwards"

    def __init__ (self ,*,peer :"raw.base.InputPeer",enabled :bool )->None :
        self .peer =peer 
        self .enabled =enabled 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ToggleNoForwards":

        peer =TLObject .read (b )

        enabled =Bool .read (b )

        return ToggleNoForwards (peer =peer ,enabled =enabled )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Bool (self .enabled ))

        return b .getvalue ()
