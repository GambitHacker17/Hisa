
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdatePasswordSettings (TLObject ):
    """"""

    __slots__ :List [str ]=["password","new_settings"]

    ID =0xa59b102f 
    QUALNAME ="functions.account.UpdatePasswordSettings"

    def __init__ (self ,*,password :"raw.base.InputCheckPasswordSRP",new_settings :"raw.base.account.PasswordInputSettings")->None :
        self .password =password 
        self .new_settings =new_settings 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdatePasswordSettings":

        password =TLObject .read (b )

        new_settings =TLObject .read (b )

        return UpdatePasswordSettings (password =password ,new_settings =new_settings )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .password .write ())

        b .write (self .new_settings .write ())

        return b .getvalue ()
