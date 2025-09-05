
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class BindAuthKeyInner (TLObject ):
    """"""

    __slots__ :List [str ]=["nonce","temp_auth_key_id","perm_auth_key_id","temp_session_id","expires_at"]

    ID =0x75a3f765 
    QUALNAME ="types.BindAuthKeyInner"

    def __init__ (self ,*,nonce :int ,temp_auth_key_id :int ,perm_auth_key_id :int ,temp_session_id :int ,expires_at :int )->None :
        self .nonce =nonce 
        self .temp_auth_key_id =temp_auth_key_id 
        self .perm_auth_key_id =perm_auth_key_id 
        self .temp_session_id =temp_session_id 
        self .expires_at =expires_at 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"BindAuthKeyInner":

        nonce =Long .read (b )

        temp_auth_key_id =Long .read (b )

        perm_auth_key_id =Long .read (b )

        temp_session_id =Long .read (b )

        expires_at =Int .read (b )

        return BindAuthKeyInner (nonce =nonce ,temp_auth_key_id =temp_auth_key_id ,perm_auth_key_id =perm_auth_key_id ,temp_session_id =temp_session_id ,expires_at =expires_at )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .nonce ))

        b .write (Long (self .temp_auth_key_id ))

        b .write (Long (self .perm_auth_key_id ))

        b .write (Long (self .temp_session_id ))

        b .write (Int (self .expires_at ))

        return b .getvalue ()
