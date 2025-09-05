
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SetContactSignUpNotification (TLObject ):
    """"""

    __slots__ :List [str ]=["silent"]

    ID =0xcff43f61 
    QUALNAME ="functions.account.SetContactSignUpNotification"

    def __init__ (self ,*,silent :bool )->None :
        self .silent =silent 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SetContactSignUpNotification":

        silent =Bool .read (b )

        return SetContactSignUpNotification (silent =silent )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Bool (self .silent ))

        return b .getvalue ()
