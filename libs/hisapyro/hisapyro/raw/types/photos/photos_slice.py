
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PhotosSlice (TLObject ):
    """"""

    __slots__ :List [str ]=["count","photos","users"]

    ID =0x15051f54 
    QUALNAME ="types.photos.PhotosSlice"

    def __init__ (self ,*,count :int ,photos :List ["raw.base.Photo"],users :List ["raw.base.User"])->None :
        self .count =count 
        self .photos =photos 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PhotosSlice":

        count =Int .read (b )

        photos =TLObject .read (b )

        users =TLObject .read (b )

        return PhotosSlice (count =count ,photos =photos ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .count ))

        b .write (Vector (self .photos ))

        b .write (Vector (self .users ))

        return b .getvalue ()
