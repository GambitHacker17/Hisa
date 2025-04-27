
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PageTableRow (TLObject ):
    """"""

    __slots__ :List [str ]=["cells"]

    ID =0xe0c0c5e5 
    QUALNAME ="types.PageTableRow"

    def __init__ (self ,*,cells :List ["raw.base.PageTableCell"])->None :
        self .cells =cells 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PageTableRow":

        cells =TLObject .read (b )

        return PageTableRow (cells =cells )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .cells ))

        return b .getvalue ()
