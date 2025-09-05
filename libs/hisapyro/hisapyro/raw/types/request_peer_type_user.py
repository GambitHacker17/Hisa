
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class RequestPeerTypeUser (TLObject ):
    """"""

    __slots__ :List [str ]=["bot","premium"]

    ID =0x5f3b8a00 
    QUALNAME ="types.RequestPeerTypeUser"

    def __init__ (self ,*,bot :Optional [bool ]=None ,premium :Optional [bool ]=None )->None :
        self .bot =bot 
        self .premium =premium 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"RequestPeerTypeUser":

        flags =Int .read (b )

        bot =Bool .read (b )if flags &(1 <<0 )else None 
        premium =Bool .read (b )if flags &(1 <<1 )else None 
        return RequestPeerTypeUser (bot =bot ,premium =premium )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .bot is not None else 0 
        flags |=(1 <<1 )if self .premium is not None else 0 
        b .write (Int (flags ))

        if self .bot is not None :
            b .write (Bool (self .bot ))

        if self .premium is not None :
            b .write (Bool (self .premium ))

        return b .getvalue ()
