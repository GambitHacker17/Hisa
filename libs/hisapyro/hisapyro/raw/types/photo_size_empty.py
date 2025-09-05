
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PhotoSizeEmpty (TLObject ):
    """"""

    __slots__ :List [str ]=["type"]

    ID =0xe17e23c 
    QUALNAME ="types.PhotoSizeEmpty"

    def __init__ (self ,*,type :str )->None :
        self .type =type 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PhotoSizeEmpty":

        type =String .read (b )

        return PhotoSizeEmpty (type =type )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .type ))

        return b .getvalue ()
