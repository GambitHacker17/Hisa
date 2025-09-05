
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DhGenOk (TLObject ):
    """"""

    __slots__ :List [str ]=["nonce","server_nonce","new_nonce_hash1"]

    ID =0x3bcbf734 
    QUALNAME ="types.DhGenOk"

    def __init__ (self ,*,nonce :int ,server_nonce :int ,new_nonce_hash1 :int )->None :
        self .nonce =nonce 
        self .server_nonce =server_nonce 
        self .new_nonce_hash1 =new_nonce_hash1 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DhGenOk":

        nonce =Int128 .read (b )

        server_nonce =Int128 .read (b )

        new_nonce_hash1 =Int128 .read (b )

        return DhGenOk (nonce =nonce ,server_nonce =server_nonce ,new_nonce_hash1 =new_nonce_hash1 )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int128 (self .nonce ))

        b .write (Int128 (self .server_nonce ))

        b .write (Int128 (self .new_nonce_hash1 ))

        return b .getvalue ()
