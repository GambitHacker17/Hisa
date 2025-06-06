
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UserStatusOffline (TLObject ):
    """"""

    __slots__ :List [str ]=["was_online"]

    ID =0x8c703f 
    QUALNAME ="types.UserStatusOffline"

    def __init__ (self ,*,was_online :int )->None :
        self .was_online =was_online 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UserStatusOffline":

        was_online =Int .read (b )

        return UserStatusOffline (was_online =was_online )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .was_online ))

        return b .getvalue ()
