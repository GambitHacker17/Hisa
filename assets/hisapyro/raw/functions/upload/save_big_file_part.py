
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SaveBigFilePart (TLObject ):
    """"""

    __slots__ :List [str ]=["file_id","file_part","file_total_parts","bytes"]

    ID =0xde7b673d 
    QUALNAME ="functions.upload.SaveBigFilePart"

    def __init__ (self ,*,file_id :int ,file_part :int ,file_total_parts :int ,bytes :bytes )->None :
        self .file_id =file_id 
        self .file_part =file_part 
        self .file_total_parts =file_total_parts 
        self .bytes =bytes 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SaveBigFilePart":

        file_id =Long .read (b )

        file_part =Int .read (b )

        file_total_parts =Int .read (b )

        bytes =Bytes .read (b )

        return SaveBigFilePart (file_id =file_id ,file_part =file_part ,file_total_parts =file_total_parts ,bytes =bytes )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .file_id ))

        b .write (Int (self .file_part ))

        b .write (Int (self .file_total_parts ))

        b .write (Bytes (self .bytes ))

        return b .getvalue ()
