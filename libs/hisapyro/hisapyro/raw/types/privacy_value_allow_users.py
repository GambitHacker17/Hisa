
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PrivacyValueAllowUsers (TLObject ):
    """"""

    __slots__ :List [str ]=["users"]

    ID =0xb8905fb2 
    QUALNAME ="types.PrivacyValueAllowUsers"

    def __init__ (self ,*,users :List [int ])->None :
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PrivacyValueAllowUsers":

        users =TLObject .read (b ,Long )

        return PrivacyValueAllowUsers (users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .users ,Long ))

        return b .getvalue ()
