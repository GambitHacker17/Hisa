
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ToggleTopPeers (TLObject ):
    """"""

    __slots__ :List [str ]=["enabled"]

    ID =0x8514bdda 
    QUALNAME ="functions.contacts.ToggleTopPeers"

    def __init__ (self ,*,enabled :bool )->None :
        self .enabled =enabled 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ToggleTopPeers":

        enabled =Bool .read (b )

        return ToggleTopPeers (enabled =enabled )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Bool (self .enabled ))

        return b .getvalue ()
