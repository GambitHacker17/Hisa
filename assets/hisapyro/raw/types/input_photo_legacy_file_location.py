
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputPhotoLegacyFileLocation (TLObject ):
    """"""

    __slots__ :List [str ]=["id","access_hash","file_reference","volume_id","local_id","secret"]

    ID =0xd83466f3 
    QUALNAME ="types.InputPhotoLegacyFileLocation"

    def __init__ (self ,*,id :int ,access_hash :int ,file_reference :bytes ,volume_id :int ,local_id :int ,secret :int )->None :
        self .id =id 
        self .access_hash =access_hash 
        self .file_reference =file_reference 
        self .volume_id =volume_id 
        self .local_id =local_id 
        self .secret =secret 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputPhotoLegacyFileLocation":

        id =Long .read (b )

        access_hash =Long .read (b )

        file_reference =Bytes .read (b )

        volume_id =Long .read (b )

        local_id =Int .read (b )

        secret =Long .read (b )

        return InputPhotoLegacyFileLocation (id =id ,access_hash =access_hash ,file_reference =file_reference ,volume_id =volume_id ,local_id =local_id ,secret =secret )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .id ))

        b .write (Long (self .access_hash ))

        b .write (Bytes (self .file_reference ))

        b .write (Long (self .volume_id ))

        b .write (Int (self .local_id ))

        b .write (Long (self .secret ))

        return b .getvalue ()
