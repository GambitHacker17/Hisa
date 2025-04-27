
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ImportBotAuthorization (TLObject ):
    """"""

    __slots__ :List [str ]=["flags","api_id","api_hash","bot_auth_token"]

    ID =0x67a3ff2c 
    QUALNAME ="functions.auth.ImportBotAuthorization"

    def __init__ (self ,*,flags :int ,api_id :int ,api_hash :str ,bot_auth_token :str )->None :
        self .flags =flags 
        self .api_id =api_id 
        self .api_hash =api_hash 
        self .bot_auth_token =bot_auth_token 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ImportBotAuthorization":

        flags =Int .read (b )

        api_id =Int .read (b )

        api_hash =String .read (b )

        bot_auth_token =String .read (b )

        return ImportBotAuthorization (flags =flags ,api_id =api_id ,api_hash =api_hash ,bot_auth_token =bot_auth_token )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .flags ))

        b .write (Int (self .api_id ))

        b .write (String (self .api_hash ))

        b .write (String (self .bot_auth_token ))

        return b .getvalue ()
