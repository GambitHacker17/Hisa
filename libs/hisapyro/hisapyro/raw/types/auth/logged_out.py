
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class LoggedOut (TLObject ):
    """"""

    __slots__ :List [str ]=["future_auth_token"]

    ID =0xc3a2835f 
    QUALNAME ="types.auth.LoggedOut"

    def __init__ (self ,*,future_auth_token :Optional [bytes ]=None )->None :
        self .future_auth_token =future_auth_token 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"LoggedOut":

        flags =Int .read (b )

        future_auth_token =Bytes .read (b )if flags &(1 <<0 )else None 
        return LoggedOut (future_auth_token =future_auth_token )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .future_auth_token is not None else 0 
        b .write (Int (flags ))

        if self .future_auth_token is not None :
            b .write (Bytes (self .future_auth_token ))

        return b .getvalue ()
