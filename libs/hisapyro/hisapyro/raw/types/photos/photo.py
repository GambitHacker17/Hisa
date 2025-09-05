
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Photo (TLObject ):
    """"""

    __slots__ :List [str ]=["photo","users"]

    ID =0x20212ca8 
    QUALNAME ="types.photos.Photo"

    def __init__ (self ,*,photo :"raw.base.Photo",users :List ["raw.base.User"])->None :
        self .photo =photo 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Photo":

        photo =TLObject .read (b )

        users =TLObject .read (b )

        return Photo (photo =photo ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .photo .write ())

        b .write (Vector (self .users ))

        return b .getvalue ()
