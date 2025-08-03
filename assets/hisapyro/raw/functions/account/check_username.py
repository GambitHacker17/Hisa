
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class CheckUsername (TLObject ):
    """"""

    __slots__ :List [str ]=["username"]

    ID =0x2714d86c 
    QUALNAME ="functions.account.CheckUsername"

    def __init__ (self ,*,username :str )->None :
        self .username =username 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"CheckUsername":

        username =String .read (b )

        return CheckUsername (username =username )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .username ))

        return b .getvalue ()
