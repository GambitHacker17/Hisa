
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DhGenFail (TLObject ):
    """"""

    __slots__ :List [str ]=["nonce","server_nonce","new_nonce_hash3"]

    ID =0xa69dae02 
    QUALNAME ="types.DhGenFail"

    def __init__ (self ,*,nonce :int ,server_nonce :int ,new_nonce_hash3 :int )->None :
        self .nonce =nonce 
        self .server_nonce =server_nonce 
        self .new_nonce_hash3 =new_nonce_hash3 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DhGenFail":

        nonce =Int128 .read (b )

        server_nonce =Int128 .read (b )

        new_nonce_hash3 =Int128 .read (b )

        return DhGenFail (nonce =nonce ,server_nonce =server_nonce ,new_nonce_hash3 =new_nonce_hash3 )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int128 (self .nonce ))

        b .write (Int128 (self .server_nonce ))

        b .write (Int128 (self .new_nonce_hash3 ))

        return b .getvalue ()
