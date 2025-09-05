
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SearchResultsPositions (TLObject ):
    """"""

    __slots__ :List [str ]=["count","positions"]

    ID =0x53b22baf 
    QUALNAME ="types.messages.SearchResultsPositions"

    def __init__ (self ,*,count :int ,positions :List ["raw.base.SearchResultsPosition"])->None :
        self .count =count 
        self .positions =positions 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SearchResultsPositions":

        count =Int .read (b )

        positions =TLObject .read (b )

        return SearchResultsPositions (count =count ,positions =positions )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .count ))

        b .write (Vector (self .positions ))

        return b .getvalue ()
