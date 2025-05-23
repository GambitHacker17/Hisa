
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PasswordInputSettings (TLObject ):
    """"""

    __slots__ :List [str ]=["new_algo","new_password_hash","hint","email","new_secure_settings"]

    ID =0xc23727c9 
    QUALNAME ="types.account.PasswordInputSettings"

    def __init__ (self ,*,new_algo :"raw.base.PasswordKdfAlgo"=None ,new_password_hash :Optional [bytes ]=None ,hint :Optional [str ]=None ,email :Optional [str ]=None ,new_secure_settings :"raw.base.SecureSecretSettings"=None )->None :
        self .new_algo =new_algo 
        self .new_password_hash =new_password_hash 
        self .hint =hint 
        self .email =email 
        self .new_secure_settings =new_secure_settings 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PasswordInputSettings":

        flags =Int .read (b )

        new_algo =TLObject .read (b )if flags &(1 <<0 )else None 

        new_password_hash =Bytes .read (b )if flags &(1 <<0 )else None 
        hint =String .read (b )if flags &(1 <<0 )else None 
        email =String .read (b )if flags &(1 <<1 )else None 
        new_secure_settings =TLObject .read (b )if flags &(1 <<2 )else None 

        return PasswordInputSettings (new_algo =new_algo ,new_password_hash =new_password_hash ,hint =hint ,email =email ,new_secure_settings =new_secure_settings )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .new_algo is not None else 0 
        flags |=(1 <<0 )if self .new_password_hash is not None else 0 
        flags |=(1 <<0 )if self .hint is not None else 0 
        flags |=(1 <<1 )if self .email is not None else 0 
        flags |=(1 <<2 )if self .new_secure_settings is not None else 0 
        b .write (Int (flags ))

        if self .new_algo is not None :
            b .write (self .new_algo .write ())

        if self .new_password_hash is not None :
            b .write (Bytes (self .new_password_hash ))

        if self .hint is not None :
            b .write (String (self .hint ))

        if self .email is not None :
            b .write (String (self .email ))

        if self .new_secure_settings is not None :
            b .write (self .new_secure_settings .write ())

        return b .getvalue ()
