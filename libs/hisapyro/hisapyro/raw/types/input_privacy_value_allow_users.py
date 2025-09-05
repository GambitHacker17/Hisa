
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputPrivacyValueAllowUsers (TLObject ):
    """"""

    __slots__ :List [str ]=["users"]

    ID =0x131cc67f 
    QUALNAME ="types.InputPrivacyValueAllowUsers"

    def __init__ (self ,*,users :List ["raw.base.InputUser"])->None :
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputPrivacyValueAllowUsers":

        users =TLObject .read (b )

        return InputPrivacyValueAllowUsers (users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .users ))

        return b .getvalue ()
