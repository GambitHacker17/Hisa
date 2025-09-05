
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PageBlockRelatedArticles (TLObject ):
    """"""

    __slots__ :List [str ]=["title","articles"]

    ID =0x16115a96 
    QUALNAME ="types.PageBlockRelatedArticles"

    def __init__ (self ,*,title :"raw.base.RichText",articles :List ["raw.base.PageRelatedArticle"])->None :
        self .title =title 
        self .articles =articles 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PageBlockRelatedArticles":

        title =TLObject .read (b )

        articles =TLObject .read (b )

        return PageBlockRelatedArticles (title =title ,articles =articles )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .title .write ())

        b .write (Vector (self .articles ))

        return b .getvalue ()
