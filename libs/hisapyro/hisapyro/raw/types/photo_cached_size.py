
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PhotoCachedSize (TLObject ):
    """"""

    __slots__ :List [str ]=["type","w","h","bytes"]

    ID =0x21e1ad6 
    QUALNAME ="types.PhotoCachedSize"

    def __init__ (self ,*,type :str ,w :int ,h :int ,bytes :bytes )->None :
        self .type =type 
        self .w =w 
        self .h =h 
        self .bytes =bytes 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PhotoCachedSize":

        type =String .read (b )

        w =Int .read (b )

        h =Int .read (b )

        bytes =Bytes .read (b )

        return PhotoCachedSize (type =type ,w =w ,h =h ,bytes =bytes )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .type ))

        b .write (Int (self .w ))

        b .write (Int (self .h ))

        b .write (Bytes (self .bytes ))

        return b .getvalue ()
