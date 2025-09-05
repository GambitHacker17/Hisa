
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetAvailableReactions (TLObject ):
    """"""

    __slots__ :List [str ]=["hash"]

    ID =0x18dea0ac 
    QUALNAME ="functions.messages.GetAvailableReactions"

    def __init__ (self ,*,hash :int )->None :
        self .hash =hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetAvailableReactions":

        hash =Int .read (b )

        return GetAvailableReactions (hash =hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .hash ))

        return b .getvalue ()
