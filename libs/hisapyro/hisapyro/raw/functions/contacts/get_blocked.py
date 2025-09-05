
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetBlocked (TLObject ):
    """"""

    __slots__ :List [str ]=["offset","limit"]

    ID =0xf57c350f 
    QUALNAME ="functions.contacts.GetBlocked"

    def __init__ (self ,*,offset :int ,limit :int )->None :
        self .offset =offset 
        self .limit =limit 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetBlocked":

        offset =Int .read (b )

        limit =Int .read (b )

        return GetBlocked (offset =offset ,limit =limit )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .offset ))

        b .write (Int (self .limit ))

        return b .getvalue ()
