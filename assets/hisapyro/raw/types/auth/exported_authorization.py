
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ExportedAuthorization (TLObject ):
    """"""

    __slots__ :List [str ]=["id","bytes"]

    ID =0xb434e2b8 
    QUALNAME ="types.auth.ExportedAuthorization"

    def __init__ (self ,*,id :int ,bytes :bytes )->None :
        self .id =id 
        self .bytes =bytes 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ExportedAuthorization":

        id =Long .read (b )

        bytes =Bytes .read (b )

        return ExportedAuthorization (id =id ,bytes =bytes )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .id ))

        b .write (Bytes (self .bytes ))

        return b .getvalue ()
