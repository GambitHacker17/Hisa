
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateUsername (TLObject ):
    """"""

    __slots__ :List [str ]=["username"]

    ID =0x3e0bdd7c 
    QUALNAME ="functions.account.UpdateUsername"

    def __init__ (self ,*,username :str )->None :
        self .username =username 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateUsername":

        username =String .read (b )

        return UpdateUsername (username =username )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .username ))

        return b .getvalue ()
