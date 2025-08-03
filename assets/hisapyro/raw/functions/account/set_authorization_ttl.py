
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SetAuthorizationTTL (TLObject ):
    """"""

    __slots__ :List [str ]=["authorization_ttl_days"]

    ID =0xbf899aa0 
    QUALNAME ="functions.account.SetAuthorizationTTL"

    def __init__ (self ,*,authorization_ttl_days :int )->None :
        self .authorization_ttl_days =authorization_ttl_days 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SetAuthorizationTTL":

        authorization_ttl_days =Int .read (b )

        return SetAuthorizationTTL (authorization_ttl_days =authorization_ttl_days )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .authorization_ttl_days ))

        return b .getvalue ()
