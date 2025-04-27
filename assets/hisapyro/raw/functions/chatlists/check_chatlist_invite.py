
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class CheckChatlistInvite (TLObject ):
    """"""

    __slots__ :List [str ]=["slug"]

    ID =0x41c10fff 
    QUALNAME ="functions.chatlists.CheckChatlistInvite"

    def __init__ (self ,*,slug :str )->None :
        self .slug =slug 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"CheckChatlistInvite":

        slug =String .read (b )

        return CheckChatlistInvite (slug =slug )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .slug ))

        return b .getvalue ()
