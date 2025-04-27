
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class CheckPassword (TLObject ):
    """"""

    __slots__ :List [str ]=["password"]

    ID =0xd18b4d16 
    QUALNAME ="functions.auth.CheckPassword"

    def __init__ (self ,*,password :"raw.base.InputCheckPasswordSRP")->None :
        self .password =password 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"CheckPassword":

        password =TLObject .read (b )

        return CheckPassword (password =password )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .password .write ())

        return b .getvalue ()
