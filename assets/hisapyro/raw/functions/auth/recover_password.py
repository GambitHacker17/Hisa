
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class RecoverPassword (TLObject ):
    """"""

    __slots__ :List [str ]=["code","new_settings"]

    ID =0x37096c70 
    QUALNAME ="functions.auth.RecoverPassword"

    def __init__ (self ,*,code :str ,new_settings :"raw.base.account.PasswordInputSettings"=None )->None :
        self .code =code 
        self .new_settings =new_settings 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"RecoverPassword":

        flags =Int .read (b )

        code =String .read (b )

        new_settings =TLObject .read (b )if flags &(1 <<0 )else None 

        return RecoverPassword (code =code ,new_settings =new_settings )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .new_settings is not None else 0 
        b .write (Int (flags ))

        b .write (String (self .code ))

        if self .new_settings is not None :
            b .write (self .new_settings .write ())

        return b .getvalue ()
