
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputDocument (TLObject ):
    """"""

    __slots__ :List [str ]=["id","access_hash","file_reference"]

    ID =0x1abfb575 
    QUALNAME ="types.InputDocument"

    def __init__ (self ,*,id :int ,access_hash :int ,file_reference :bytes )->None :
        self .id =id 
        self .access_hash =access_hash 
        self .file_reference =file_reference 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputDocument":

        id =Long .read (b )

        access_hash =Long .read (b )

        file_reference =Bytes .read (b )

        return InputDocument (id =id ,access_hash =access_hash ,file_reference =file_reference )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .id ))

        b .write (Long (self .access_hash ))

        b .write (Bytes (self .file_reference ))

        return b .getvalue ()
