
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ClientDHInnerData (TLObject ):
    """"""

    __slots__ :List [str ]=["nonce","server_nonce","retry_id","g_b"]

    ID =0x6643b654 
    QUALNAME ="types.ClientDHInnerData"

    def __init__ (self ,*,nonce :int ,server_nonce :int ,retry_id :int ,g_b :bytes )->None :
        self .nonce =nonce 
        self .server_nonce =server_nonce 
        self .retry_id =retry_id 
        self .g_b =g_b 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ClientDHInnerData":

        nonce =Int128 .read (b )

        server_nonce =Int128 .read (b )

        retry_id =Long .read (b )

        g_b =Bytes .read (b )

        return ClientDHInnerData (nonce =nonce ,server_nonce =server_nonce ,retry_id =retry_id ,g_b =g_b )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int128 (self .nonce ))

        b .write (Int128 (self .server_nonce ))

        b .write (Long (self .retry_id ))

        b .write (Bytes (self .g_b ))

        return b .getvalue ()
