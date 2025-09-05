
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DeleteSecureValue (TLObject ):
    """"""

    __slots__ :List [str ]=["types"]

    ID =0xb880bc4b 
    QUALNAME ="functions.account.DeleteSecureValue"

    def __init__ (self ,*,types :List ["raw.base.SecureValueType"])->None :
        self .types =types 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DeleteSecureValue":

        types =TLObject .read (b )

        return DeleteSecureValue (types =types )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .types ))

        return b .getvalue ()
