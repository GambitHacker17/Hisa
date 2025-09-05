
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InviteText (TLObject ):
    """"""

    __slots__ :List [str ]=["message"]

    ID =0x18cb9f78 
    QUALNAME ="types.help.InviteText"

    def __init__ (self ,*,message :str )->None :
        self .message =message 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InviteText":

        message =String .read (b )

        return InviteText (message =message )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .message ))

        return b .getvalue ()
