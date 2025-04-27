
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Search (TLObject ):
    """"""

    __slots__ :List [str ]=["q","limit"]

    ID =0x11f812d8 
    QUALNAME ="functions.contacts.Search"

    def __init__ (self ,*,q :str ,limit :int )->None :
        self .q =q 
        self .limit =limit 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Search":

        q =String .read (b )

        limit =Int .read (b )

        return Search (q =q ,limit =limit )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .q ))

        b .write (Int (self .limit ))

        return b .getvalue ()
