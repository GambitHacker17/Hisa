
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ReqDHParams (TLObject ):
    """"""

    __slots__ :List [str ]=["nonce","server_nonce","p","q","public_key_fingerprint","encrypted_data"]

    ID =0xd712e4be 
    QUALNAME ="functions.ReqDHParams"

    def __init__ (self ,*,nonce :int ,server_nonce :int ,p :bytes ,q :bytes ,public_key_fingerprint :int ,encrypted_data :bytes )->None :
        self .nonce =nonce 
        self .server_nonce =server_nonce 
        self .p =p 
        self .q =q 
        self .public_key_fingerprint =public_key_fingerprint 
        self .encrypted_data =encrypted_data 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ReqDHParams":

        nonce =Int128 .read (b )

        server_nonce =Int128 .read (b )

        p =Bytes .read (b )

        q =Bytes .read (b )

        public_key_fingerprint =Long .read (b )

        encrypted_data =Bytes .read (b )

        return ReqDHParams (nonce =nonce ,server_nonce =server_nonce ,p =p ,q =q ,public_key_fingerprint =public_key_fingerprint ,encrypted_data =encrypted_data )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int128 (self .nonce ))

        b .write (Int128 (self .server_nonce ))

        b .write (Bytes (self .p ))

        b .write (Bytes (self .q ))

        b .write (Long (self .public_key_fingerprint ))

        b .write (Bytes (self .encrypted_data ))

        return b .getvalue ()
