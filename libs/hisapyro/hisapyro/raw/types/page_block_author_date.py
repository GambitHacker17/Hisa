
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PageBlockAuthorDate (TLObject ):
    """"""

    __slots__ :List [str ]=["author","published_date"]

    ID =0xbaafe5e0 
    QUALNAME ="types.PageBlockAuthorDate"

    def __init__ (self ,*,author :"raw.base.RichText",published_date :int )->None :
        self .author =author 
        self .published_date =published_date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PageBlockAuthorDate":

        author =TLObject .read (b )

        published_date =Int .read (b )

        return PageBlockAuthorDate (author =author ,published_date =published_date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .author .write ())

        b .write (Int (self .published_date ))

        return b .getvalue ()
