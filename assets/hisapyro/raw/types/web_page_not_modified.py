
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class WebPageNotModified (TLObject ):
    """"""

    __slots__ :List [str ]=["cached_page_views"]

    ID =0x7311ca11 
    QUALNAME ="types.WebPageNotModified"

    def __init__ (self ,*,cached_page_views :Optional [int ]=None )->None :
        self .cached_page_views =cached_page_views 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"WebPageNotModified":

        flags =Int .read (b )

        cached_page_views =Int .read (b )if flags &(1 <<0 )else None 
        return WebPageNotModified (cached_page_views =cached_page_views )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .cached_page_views is not None else 0 
        b .write (Int (flags ))

        if self .cached_page_views is not None :
            b .write (Int (self .cached_page_views ))

        return b .getvalue ()
