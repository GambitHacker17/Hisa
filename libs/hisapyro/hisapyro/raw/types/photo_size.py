
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PhotoSize (TLObject ):
    """"""

    __slots__ :List [str ]=["type","w","h","size"]

    ID =0x75c78e60 
    QUALNAME ="types.PhotoSize"

    def __init__ (self ,*,type :str ,w :int ,h :int ,size :int )->None :
        self .type =type 
        self .w =w 
        self .h =h 
        self .size =size 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PhotoSize":

        type =String .read (b )

        w =Int .read (b )

        h =Int .read (b )

        size =Int .read (b )

        return PhotoSize (type =type ,w =w ,h =h ,size =size )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .type ))

        b .write (Int (self .w ))

        b .write (Int (self .h ))

        b .write (Int (self .size ))

        return b .getvalue ()
