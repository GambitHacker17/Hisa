
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ImportWebTokenAuthorization (TLObject ):
    """"""

    __slots__ :List [str ]=["api_id","api_hash","web_auth_token"]

    ID =0x2db873a9 
    QUALNAME ="functions.auth.ImportWebTokenAuthorization"

    def __init__ (self ,*,api_id :int ,api_hash :str ,web_auth_token :str )->None :
        self .api_id =api_id 
        self .api_hash =api_hash 
        self .web_auth_token =web_auth_token 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ImportWebTokenAuthorization":

        api_id =Int .read (b )

        api_hash =String .read (b )

        web_auth_token =String .read (b )

        return ImportWebTokenAuthorization (api_id =api_id ,api_hash =api_hash ,web_auth_token =web_auth_token )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .api_id ))

        b .write (String (self .api_hash ))

        b .write (String (self .web_auth_token ))

        return b .getvalue ()
