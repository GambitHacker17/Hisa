
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class LoginTokenSuccess (TLObject ):
    """"""

    __slots__ :List [str ]=["authorization"]

    ID =0x390d5c5e 
    QUALNAME ="types.auth.LoginTokenSuccess"

    def __init__ (self ,*,authorization :"raw.base.auth.Authorization")->None :
        self .authorization =authorization 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"LoginTokenSuccess":

        authorization =TLObject .read (b )

        return LoginTokenSuccess (authorization =authorization )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .authorization .write ())

        return b .getvalue ()
