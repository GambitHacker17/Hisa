
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Photos (TLObject ):
    """"""

    __slots__ :List [str ]=["photos","users"]

    ID =0x8dca6aa5 
    QUALNAME ="types.photos.Photos"

    def __init__ (self ,*,photos :List ["raw.base.Photo"],users :List ["raw.base.User"])->None :
        self .photos =photos 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Photos":

        photos =TLObject .read (b )

        users =TLObject .read (b )

        return Photos (photos =photos ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .photos ))

        b .write (Vector (self .users ))

        return b .getvalue ()
