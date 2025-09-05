
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AuthorizationSignUpRequired (TLObject ):
    """"""

    __slots__ :List [str ]=["terms_of_service"]

    ID =0x44747e9a 
    QUALNAME ="types.auth.AuthorizationSignUpRequired"

    def __init__ (self ,*,terms_of_service :"raw.base.help.TermsOfService"=None )->None :
        self .terms_of_service =terms_of_service 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AuthorizationSignUpRequired":

        flags =Int .read (b )

        terms_of_service =TLObject .read (b )if flags &(1 <<0 )else None 

        return AuthorizationSignUpRequired (terms_of_service =terms_of_service )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .terms_of_service is not None else 0 
        b .write (Int (flags ))

        if self .terms_of_service is not None :
            b .write (self .terms_of_service .write ())

        return b .getvalue ()
