
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UserStatusOnline (TLObject ):
    """"""

    __slots__ :List [str ]=["expires"]

    ID =0xedb93949 
    QUALNAME ="types.UserStatusOnline"

    def __init__ (self ,*,expires :int )->None :
        self .expires =expires 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UserStatusOnline":

        expires =Int .read (b )

        return UserStatusOnline (expires =expires )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .expires ))

        return b .getvalue ()
