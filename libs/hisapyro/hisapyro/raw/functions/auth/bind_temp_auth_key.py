
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class BindTempAuthKey (TLObject ):
    """"""

    __slots__ :List [str ]=["perm_auth_key_id","nonce","expires_at","encrypted_message"]

    ID =0xcdd42a05 
    QUALNAME ="functions.auth.BindTempAuthKey"

    def __init__ (self ,*,perm_auth_key_id :int ,nonce :int ,expires_at :int ,encrypted_message :bytes )->None :
        self .perm_auth_key_id =perm_auth_key_id 
        self .nonce =nonce 
        self .expires_at =expires_at 
        self .encrypted_message =encrypted_message 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"BindTempAuthKey":

        perm_auth_key_id =Long .read (b )

        nonce =Long .read (b )

        expires_at =Int .read (b )

        encrypted_message =Bytes .read (b )

        return BindTempAuthKey (perm_auth_key_id =perm_auth_key_id ,nonce =nonce ,expires_at =expires_at ,encrypted_message =encrypted_message )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .perm_auth_key_id ))

        b .write (Long (self .nonce ))

        b .write (Int (self .expires_at ))

        b .write (Bytes (self .encrypted_message ))

        return b .getvalue ()
