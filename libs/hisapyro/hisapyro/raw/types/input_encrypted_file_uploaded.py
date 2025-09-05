
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputEncryptedFileUploaded (TLObject ):
    """"""

    __slots__ :List [str ]=["id","parts","md5_checksum","key_fingerprint"]

    ID =0x64bd0306 
    QUALNAME ="types.InputEncryptedFileUploaded"

    def __init__ (self ,*,id :int ,parts :int ,md5_checksum :str ,key_fingerprint :int )->None :
        self .id =id 
        self .parts =parts 
        self .md5_checksum =md5_checksum 
        self .key_fingerprint =key_fingerprint 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputEncryptedFileUploaded":

        id =Long .read (b )

        parts =Int .read (b )

        md5_checksum =String .read (b )

        key_fingerprint =Int .read (b )

        return InputEncryptedFileUploaded (id =id ,parts =parts ,md5_checksum =md5_checksum ,key_fingerprint =key_fingerprint )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .id ))

        b .write (Int (self .parts ))

        b .write (String (self .md5_checksum ))

        b .write (Int (self .key_fingerprint ))

        return b .getvalue ()
