
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PQInnerDataDc (TLObject ):
    """"""

    __slots__ :List [str ]=["pq","p","q","nonce","server_nonce","new_nonce","dc"]

    ID =0xa9f55f95 
    QUALNAME ="types.PQInnerDataDc"

    def __init__ (self ,*,pq :bytes ,p :bytes ,q :bytes ,nonce :int ,server_nonce :int ,new_nonce :int ,dc :int )->None :
        self .pq =pq 
        self .p =p 
        self .q =q 
        self .nonce =nonce 
        self .server_nonce =server_nonce 
        self .new_nonce =new_nonce 
        self .dc =dc 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PQInnerDataDc":

        pq =Bytes .read (b )

        p =Bytes .read (b )

        q =Bytes .read (b )

        nonce =Int128 .read (b )

        server_nonce =Int128 .read (b )

        new_nonce =Int256 .read (b )

        dc =Int .read (b )

        return PQInnerDataDc (pq =pq ,p =p ,q =q ,nonce =nonce ,server_nonce =server_nonce ,new_nonce =new_nonce ,dc =dc )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Bytes (self .pq ))

        b .write (Bytes (self .p ))

        b .write (Bytes (self .q ))

        b .write (Int128 (self .nonce ))

        b .write (Int128 (self .server_nonce ))

        b .write (Int256 (self .new_nonce ))

        b .write (Int (self .dc ))

        return b .getvalue ()
