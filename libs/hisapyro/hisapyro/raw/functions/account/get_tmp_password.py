
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetTmpPassword (TLObject ):
    """"""

    __slots__ :List [str ]=["password","period"]

    ID =0x449e0b51 
    QUALNAME ="functions.account.GetTmpPassword"

    def __init__ (self ,*,password :"raw.base.InputCheckPasswordSRP",period :int )->None :
        self .password =password 
        self .period =period 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetTmpPassword":

        password =TLObject .read (b )

        period =Int .read (b )

        return GetTmpPassword (password =password ,period =period )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .password .write ())

        b .write (Int (self .period ))

        return b .getvalue ()
