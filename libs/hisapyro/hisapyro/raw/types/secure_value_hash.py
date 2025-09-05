
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SecureValueHash (TLObject ):
    """"""

    __slots__ :List [str ]=["type","hash"]

    ID =0xed1ecdb0 
    QUALNAME ="types.SecureValueHash"

    def __init__ (self ,*,type :"raw.base.SecureValueType",hash :bytes )->None :
        self .type =type 
        self .hash =hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SecureValueHash":

        type =TLObject .read (b )

        hash =Bytes .read (b )

        return SecureValueHash (type =type ,hash =hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .type .write ())

        b .write (Bytes (self .hash ))

        return b .getvalue ()
