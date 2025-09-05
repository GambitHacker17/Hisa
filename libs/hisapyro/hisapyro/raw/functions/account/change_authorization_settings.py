
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChangeAuthorizationSettings (TLObject ):
    """"""

    __slots__ :List [str ]=["hash","encrypted_requests_disabled","call_requests_disabled"]

    ID =0x40f48462 
    QUALNAME ="functions.account.ChangeAuthorizationSettings"

    def __init__ (self ,*,hash :int ,encrypted_requests_disabled :Optional [bool ]=None ,call_requests_disabled :Optional [bool ]=None )->None :
        self .hash =hash 
        self .encrypted_requests_disabled =encrypted_requests_disabled 
        self .call_requests_disabled =call_requests_disabled 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChangeAuthorizationSettings":

        flags =Int .read (b )

        hash =Long .read (b )

        encrypted_requests_disabled =Bool .read (b )if flags &(1 <<0 )else None 
        call_requests_disabled =Bool .read (b )if flags &(1 <<1 )else None 
        return ChangeAuthorizationSettings (hash =hash ,encrypted_requests_disabled =encrypted_requests_disabled ,call_requests_disabled =call_requests_disabled )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .encrypted_requests_disabled is not None else 0 
        flags |=(1 <<1 )if self .call_requests_disabled is not None else 0 
        b .write (Int (flags ))

        b .write (Long (self .hash ))

        if self .encrypted_requests_disabled is not None :
            b .write (Bool (self .encrypted_requests_disabled ))

        if self .call_requests_disabled is not None :
            b .write (Bool (self .call_requests_disabled ))

        return b .getvalue ()
