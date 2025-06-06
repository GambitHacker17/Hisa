
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SecureFile (TLObject ):
    """"""

    __slots__ :List [str ]=["id","access_hash","size","dc_id","date","file_hash","secret"]

    ID =0x7d09c27e 
    QUALNAME ="types.SecureFile"

    def __init__ (self ,*,id :int ,access_hash :int ,size :int ,dc_id :int ,date :int ,file_hash :bytes ,secret :bytes )->None :
        self .id =id 
        self .access_hash =access_hash 
        self .size =size 
        self .dc_id =dc_id 
        self .date =date 
        self .file_hash =file_hash 
        self .secret =secret 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SecureFile":

        id =Long .read (b )

        access_hash =Long .read (b )

        size =Long .read (b )

        dc_id =Int .read (b )

        date =Int .read (b )

        file_hash =Bytes .read (b )

        secret =Bytes .read (b )

        return SecureFile (id =id ,access_hash =access_hash ,size =size ,dc_id =dc_id ,date =date ,file_hash =file_hash ,secret =secret )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .id ))

        b .write (Long (self .access_hash ))

        b .write (Long (self .size ))

        b .write (Int (self .dc_id ))

        b .write (Int (self .date ))

        b .write (Bytes (self .file_hash ))

        b .write (Bytes (self .secret ))

        return b .getvalue ()
