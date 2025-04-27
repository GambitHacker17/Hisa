
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PageBlockCover (TLObject ):
    """"""

    __slots__ :List [str ]=["cover"]

    ID =0x39f23300 
    QUALNAME ="types.PageBlockCover"

    def __init__ (self ,*,cover :"raw.base.PageBlock")->None :
        self .cover =cover 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PageBlockCover":

        cover =TLObject .read (b )

        return PageBlockCover (cover =cover )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .cover .write ())

        return b .getvalue ()
