
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ServerDHParamsOk (TLObject ):
    """"""

    __slots__ :List [str ]=["nonce","server_nonce","encrypted_answer"]

    ID =0xd0e8075c 
    QUALNAME ="types.ServerDHParamsOk"

    def __init__ (self ,*,nonce :int ,server_nonce :int ,encrypted_answer :bytes )->None :
        self .nonce =nonce 
        self .server_nonce =server_nonce 
        self .encrypted_answer =encrypted_answer 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ServerDHParamsOk":

        nonce =Int128 .read (b )

        server_nonce =Int128 .read (b )

        encrypted_answer =Bytes .read (b )

        return ServerDHParamsOk (nonce =nonce ,server_nonce =server_nonce ,encrypted_answer =encrypted_answer )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int128 (self .nonce ))

        b .write (Int128 (self .server_nonce ))

        b .write (Bytes (self .encrypted_answer ))

        return b .getvalue ()
