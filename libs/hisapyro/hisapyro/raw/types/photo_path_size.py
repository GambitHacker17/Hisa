
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PhotoPathSize (TLObject ):
    """"""

    __slots__ :List [str ]=["type","bytes"]

    ID =0xd8214d41 
    QUALNAME ="types.PhotoPathSize"

    def __init__ (self ,*,type :str ,bytes :bytes )->None :
        self .type =type 
        self .bytes =bytes 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PhotoPathSize":

        type =String .read (b )

        bytes =Bytes .read (b )

        return PhotoPathSize (type =type ,bytes =bytes )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .type ))

        b .write (Bytes (self .bytes ))

        return b .getvalue ()
