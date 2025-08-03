
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ServerDHInnerData (TLObject ):
    """"""

    __slots__ :List [str ]=["nonce","server_nonce","g","dh_prime","g_a","server_time"]

    ID =0xb5890dba 
    QUALNAME ="types.ServerDHInnerData"

    def __init__ (self ,*,nonce :int ,server_nonce :int ,g :int ,dh_prime :bytes ,g_a :bytes ,server_time :int )->None :
        self .nonce =nonce 
        self .server_nonce =server_nonce 
        self .g =g 
        self .dh_prime =dh_prime 
        self .g_a =g_a 
        self .server_time =server_time 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ServerDHInnerData":

        nonce =Int128 .read (b )

        server_nonce =Int128 .read (b )

        g =Int .read (b )

        dh_prime =Bytes .read (b )

        g_a =Bytes .read (b )

        server_time =Int .read (b )

        return ServerDHInnerData (nonce =nonce ,server_nonce =server_nonce ,g =g ,dh_prime =dh_prime ,g_a =g_a ,server_time =server_time )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int128 (self .nonce ))

        b .write (Int128 (self .server_nonce ))

        b .write (Int (self .g ))

        b .write (Bytes (self .dh_prime ))

        b .write (Bytes (self .g_a ))

        b .write (Int (self .server_time ))

        return b .getvalue ()
