
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PQInnerDataTempDc (TLObject ):
    """"""

    __slots__ :List [str ]=["pq","p","q","nonce","server_nonce","new_nonce","dc","expires_in"]

    ID =0x56fddf88 
    QUALNAME ="types.PQInnerDataTempDc"

    def __init__ (self ,*,pq :bytes ,p :bytes ,q :bytes ,nonce :int ,server_nonce :int ,new_nonce :int ,dc :int ,expires_in :int )->None :
        self .pq =pq 
        self .p =p 
        self .q =q 
        self .nonce =nonce 
        self .server_nonce =server_nonce 
        self .new_nonce =new_nonce 
        self .dc =dc 
        self .expires_in =expires_in 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PQInnerDataTempDc":

        pq =Bytes .read (b )

        p =Bytes .read (b )

        q =Bytes .read (b )

        nonce =Int128 .read (b )

        server_nonce =Int128 .read (b )

        new_nonce =Int256 .read (b )

        dc =Int .read (b )

        expires_in =Int .read (b )

        return PQInnerDataTempDc (pq =pq ,p =p ,q =q ,nonce =nonce ,server_nonce =server_nonce ,new_nonce =new_nonce ,dc =dc ,expires_in =expires_in )

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

        b .write (Int (self .expires_in ))

        return b .getvalue ()
