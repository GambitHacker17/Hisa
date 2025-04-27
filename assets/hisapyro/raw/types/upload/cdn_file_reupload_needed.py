
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class CdnFileReuploadNeeded (TLObject ):
    """"""

    __slots__ :List [str ]=["request_token"]

    ID =0xeea8e46e 
    QUALNAME ="types.upload.CdnFileReuploadNeeded"

    def __init__ (self ,*,request_token :bytes )->None :
        self .request_token =request_token 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"CdnFileReuploadNeeded":

        request_token =Bytes .read (b )

        return CdnFileReuploadNeeded (request_token =request_token )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Bytes (self .request_token ))

        return b .getvalue ()
