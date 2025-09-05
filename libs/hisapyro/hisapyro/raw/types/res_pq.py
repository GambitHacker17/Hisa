
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ResPQ (TLObject ):
    """"""

    __slots__ :List [str ]=["nonce","server_nonce","pq","server_public_key_fingerprints"]

    ID =0x05162463 
    QUALNAME ="types.ResPQ"

    def __init__ (self ,*,nonce :int ,server_nonce :int ,pq :bytes ,server_public_key_fingerprints :List [int ])->None :
        self .nonce =nonce 
        self .server_nonce =server_nonce 
        self .pq =pq 
        self .server_public_key_fingerprints =server_public_key_fingerprints 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ResPQ":

        nonce =Int128 .read (b )

        server_nonce =Int128 .read (b )

        pq =Bytes .read (b )

        server_public_key_fingerprints =TLObject .read (b ,Long )

        return ResPQ (nonce =nonce ,server_nonce =server_nonce ,pq =pq ,server_public_key_fingerprints =server_public_key_fingerprints )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int128 (self .nonce ))

        b .write (Int128 (self .server_nonce ))

        b .write (Bytes (self .pq ))

        b .write (Vector (self .server_public_key_fingerprints ,Long ))

        return b .getvalue ()
