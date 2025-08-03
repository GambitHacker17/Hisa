
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class WebAuthorizations (TLObject ):
    """"""

    __slots__ :List [str ]=["authorizations","users"]

    ID =0xed56c9fc 
    QUALNAME ="types.account.WebAuthorizations"

    def __init__ (self ,*,authorizations :List ["raw.base.WebAuthorization"],users :List ["raw.base.User"])->None :
        self .authorizations =authorizations 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"WebAuthorizations":

        authorizations =TLObject .read (b )

        users =TLObject .read (b )

        return WebAuthorizations (authorizations =authorizations ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .authorizations ))

        b .write (Vector (self .users ))

        return b .getvalue ()
