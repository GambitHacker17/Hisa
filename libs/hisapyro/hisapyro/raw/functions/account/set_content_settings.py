
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SetContentSettings (TLObject ):
    """"""

    __slots__ :List [str ]=["sensitive_enabled"]

    ID =0xb574b16b 
    QUALNAME ="functions.account.SetContentSettings"

    def __init__ (self ,*,sensitive_enabled :Optional [bool ]=None )->None :
        self .sensitive_enabled =sensitive_enabled 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SetContentSettings":

        flags =Int .read (b )

        sensitive_enabled =True if flags &(1 <<0 )else False 
        return SetContentSettings (sensitive_enabled =sensitive_enabled )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .sensitive_enabled else 0 
        b .write (Int (flags ))

        return b .getvalue ()
