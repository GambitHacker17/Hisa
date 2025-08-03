
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PasswordSettings (TLObject ):
    """"""

    __slots__ :List [str ]=["email","secure_settings"]

    ID =0x9a5c33e5 
    QUALNAME ="types.account.PasswordSettings"

    def __init__ (self ,*,email :Optional [str ]=None ,secure_settings :"raw.base.SecureSecretSettings"=None )->None :
        self .email =email 
        self .secure_settings =secure_settings 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PasswordSettings":

        flags =Int .read (b )

        email =String .read (b )if flags &(1 <<0 )else None 
        secure_settings =TLObject .read (b )if flags &(1 <<1 )else None 

        return PasswordSettings (email =email ,secure_settings =secure_settings )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .email is not None else 0 
        flags |=(1 <<1 )if self .secure_settings is not None else 0 
        b .write (Int (flags ))

        if self .email is not None :
            b .write (String (self .email ))

        if self .secure_settings is not None :
            b .write (self .secure_settings .write ())

        return b .getvalue ()
