
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ContentSettings (TLObject ):
    """"""

    __slots__ :List [str ]=["sensitive_enabled","sensitive_can_change"]

    ID =0x57e28221 
    QUALNAME ="types.account.ContentSettings"

    def __init__ (self ,*,sensitive_enabled :Optional [bool ]=None ,sensitive_can_change :Optional [bool ]=None )->None :
        self .sensitive_enabled =sensitive_enabled 
        self .sensitive_can_change =sensitive_can_change 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ContentSettings":

        flags =Int .read (b )

        sensitive_enabled =True if flags &(1 <<0 )else False 
        sensitive_can_change =True if flags &(1 <<1 )else False 
        return ContentSettings (sensitive_enabled =sensitive_enabled ,sensitive_can_change =sensitive_can_change )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .sensitive_enabled else 0 
        flags |=(1 <<1 )if self .sensitive_can_change else 0 
        b .write (Int (flags ))

        return b .getvalue ()
