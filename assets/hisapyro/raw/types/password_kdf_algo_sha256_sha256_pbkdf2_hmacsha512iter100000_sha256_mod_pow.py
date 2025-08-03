
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow (TLObject ):
    """"""

    __slots__ :List [str ]=["salt1","salt2","g","p"]

    ID =0x3a912d4a 
    QUALNAME ="types.PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow"

    def __init__ (self ,*,salt1 :bytes ,salt2 :bytes ,g :int ,p :bytes )->None :
        self .salt1 =salt1 
        self .salt2 =salt2 
        self .g =g 
        self .p =p 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow":

        salt1 =Bytes .read (b )

        salt2 =Bytes .read (b )

        g =Int .read (b )

        p =Bytes .read (b )

        return PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow (salt1 =salt1 ,salt2 =salt2 ,g =g ,p =p )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Bytes (self .salt1 ))

        b .write (Bytes (self .salt2 ))

        b .write (Int (self .g ))

        b .write (Bytes (self .p ))

        return b .getvalue ()
