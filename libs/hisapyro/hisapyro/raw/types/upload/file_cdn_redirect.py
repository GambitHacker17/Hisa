
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class FileCdnRedirect (TLObject ):
    """"""

    __slots__ :List [str ]=["dc_id","file_token","encryption_key","encryption_iv","file_hashes"]

    ID =0xf18cda44 
    QUALNAME ="types.upload.FileCdnRedirect"

    def __init__ (self ,*,dc_id :int ,file_token :bytes ,encryption_key :bytes ,encryption_iv :bytes ,file_hashes :List ["raw.base.FileHash"])->None :
        self .dc_id =dc_id 
        self .file_token =file_token 
        self .encryption_key =encryption_key 
        self .encryption_iv =encryption_iv 
        self .file_hashes =file_hashes 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"FileCdnRedirect":

        dc_id =Int .read (b )

        file_token =Bytes .read (b )

        encryption_key =Bytes .read (b )

        encryption_iv =Bytes .read (b )

        file_hashes =TLObject .read (b )

        return FileCdnRedirect (dc_id =dc_id ,file_token =file_token ,encryption_key =encryption_key ,encryption_iv =encryption_iv ,file_hashes =file_hashes )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .dc_id ))

        b .write (Bytes (self .file_token ))

        b .write (Bytes (self .encryption_key ))

        b .write (Bytes (self .encryption_iv ))

        b .write (Vector (self .file_hashes ))

        return b .getvalue ()
