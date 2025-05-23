
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DeleteAccount (TLObject ):
    """"""

    __slots__ :List [str ]=["reason","password"]

    ID =0xa2c0cf74 
    QUALNAME ="functions.account.DeleteAccount"

    def __init__ (self ,*,reason :str ,password :"raw.base.InputCheckPasswordSRP"=None )->None :
        self .reason =reason 
        self .password =password 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DeleteAccount":

        flags =Int .read (b )

        reason =String .read (b )

        password =TLObject .read (b )if flags &(1 <<0 )else None 

        return DeleteAccount (reason =reason ,password =password )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .password is not None else 0 
        b .write (Int (flags ))

        b .write (String (self .reason ))

        if self .password is not None :
            b .write (self .password .write ())

        return b .getvalue ()
