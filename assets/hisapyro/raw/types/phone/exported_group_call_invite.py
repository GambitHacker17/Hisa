
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ExportedGroupCallInvite (TLObject ):
    """"""

    __slots__ :List [str ]=["link"]

    ID =0x204bd158 
    QUALNAME ="types.phone.ExportedGroupCallInvite"

    def __init__ (self ,*,link :str )->None :
        self .link =link 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ExportedGroupCallInvite":

        link =String .read (b )

        return ExportedGroupCallInvite (link =link )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .link ))

        return b .getvalue ()
