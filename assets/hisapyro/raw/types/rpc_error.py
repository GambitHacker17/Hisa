
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class RpcError (TLObject ):
    """"""

    __slots__ :List [str ]=["error_code","error_message"]

    ID =0x2144ca19 
    QUALNAME ="types.RpcError"

    def __init__ (self ,*,error_code :int ,error_message :str )->None :
        self .error_code =error_code 
        self .error_message =error_message 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"RpcError":

        error_code =Int .read (b )

        error_message =String .read (b )

        return RpcError (error_code =error_code ,error_message =error_message )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .error_code ))

        b .write (String (self .error_message ))

        return b .getvalue ()
