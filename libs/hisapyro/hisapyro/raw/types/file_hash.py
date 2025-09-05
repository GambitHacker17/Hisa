
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class FileHash (TLObject ):
    """"""

    __slots__ :List [str ]=["offset","limit","hash"]

    ID =0xf39b035c 
    QUALNAME ="types.FileHash"

    def __init__ (self ,*,offset :int ,limit :int ,hash :bytes )->None :
        self .offset =offset 
        self .limit =limit 
        self .hash =hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"FileHash":

        offset =Long .read (b )

        limit =Int .read (b )

        hash =Bytes .read (b )

        return FileHash (offset =offset ,limit =limit ,hash =hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .offset ))

        b .write (Int (self .limit ))

        b .write (Bytes (self .hash ))

        return b .getvalue ()
