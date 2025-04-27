
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class TmpPassword (TLObject ):
    """"""

    __slots__ :List [str ]=["tmp_password","valid_until"]

    ID =0xdb64fd34 
    QUALNAME ="types.account.TmpPassword"

    def __init__ (self ,*,tmp_password :bytes ,valid_until :int )->None :
        self .tmp_password =tmp_password 
        self .valid_until =valid_until 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"TmpPassword":

        tmp_password =Bytes .read (b )

        valid_until =Int .read (b )

        return TmpPassword (tmp_password =tmp_password ,valid_until =valid_until )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Bytes (self .tmp_password ))

        b .write (Int (self .valid_until ))

        return b .getvalue ()
