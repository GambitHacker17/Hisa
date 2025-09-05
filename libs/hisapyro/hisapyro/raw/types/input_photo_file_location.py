
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputPhotoFileLocation (TLObject ):
    """"""

    __slots__ :List [str ]=["id","access_hash","file_reference","thumb_size"]

    ID =0x40181ffe 
    QUALNAME ="types.InputPhotoFileLocation"

    def __init__ (self ,*,id :int ,access_hash :int ,file_reference :bytes ,thumb_size :str )->None :
        self .id =id 
        self .access_hash =access_hash 
        self .file_reference =file_reference 
        self .thumb_size =thumb_size 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputPhotoFileLocation":

        id =Long .read (b )

        access_hash =Long .read (b )

        file_reference =Bytes .read (b )

        thumb_size =String .read (b )

        return InputPhotoFileLocation (id =id ,access_hash =access_hash ,file_reference =file_reference ,thumb_size =thumb_size )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .id ))

        b .write (Long (self .access_hash ))

        b .write (Bytes (self .file_reference ))

        b .write (String (self .thumb_size ))

        return b .getvalue ()
