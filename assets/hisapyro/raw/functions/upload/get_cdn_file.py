
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetCdnFile (TLObject ):
    """"""

    __slots__ :List [str ]=["file_token","offset","limit"]

    ID =0x395f69da 
    QUALNAME ="functions.upload.GetCdnFile"

    def __init__ (self ,*,file_token :bytes ,offset :int ,limit :int )->None :
        self .file_token =file_token 
        self .offset =offset 
        self .limit =limit 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetCdnFile":

        file_token =Bytes .read (b )

        offset =Long .read (b )

        limit =Int .read (b )

        return GetCdnFile (file_token =file_token ,offset =offset ,limit =limit )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Bytes (self .file_token ))

        b .write (Long (self .offset ))

        b .write (Int (self .limit ))

        return b .getvalue ()
