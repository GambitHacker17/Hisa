
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DropTempAuthKeys (TLObject ):
    """"""

    __slots__ :List [str ]=["except_auth_keys"]

    ID =0x8e48a188 
    QUALNAME ="functions.auth.DropTempAuthKeys"

    def __init__ (self ,*,except_auth_keys :List [int ])->None :
        self .except_auth_keys =except_auth_keys 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DropTempAuthKeys":

        except_auth_keys =TLObject .read (b ,Long )

        return DropTempAuthKeys (except_auth_keys =except_auth_keys )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .except_auth_keys ,Long ))

        return b .getvalue ()
