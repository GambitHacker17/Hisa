
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PageBlockTable (TLObject ):
    """"""

    __slots__ :List [str ]=["title","rows","bordered","striped"]

    ID =0xbf4dea82 
    QUALNAME ="types.PageBlockTable"

    def __init__ (self ,*,title :"raw.base.RichText",rows :List ["raw.base.PageTableRow"],bordered :Optional [bool ]=None ,striped :Optional [bool ]=None )->None :
        self .title =title 
        self .rows =rows 
        self .bordered =bordered 
        self .striped =striped 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PageBlockTable":

        flags =Int .read (b )

        bordered =True if flags &(1 <<0 )else False 
        striped =True if flags &(1 <<1 )else False 
        title =TLObject .read (b )

        rows =TLObject .read (b )

        return PageBlockTable (title =title ,rows =rows ,bordered =bordered ,striped =striped )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .bordered else 0 
        flags |=(1 <<1 )if self .striped else 0 
        b .write (Int (flags ))

        b .write (self .title .write ())

        b .write (Vector (self .rows ))

        return b .getvalue ()
