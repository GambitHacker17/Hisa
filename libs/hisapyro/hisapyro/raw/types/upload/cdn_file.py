
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class CdnFile (TLObject ):
    """"""

    __slots__ :List [str ]=["bytes"]

    ID =0xa99fca4f 
    QUALNAME ="types.upload.CdnFile"

    def __init__ (self ,*,bytes :bytes )->None :
        self .bytes =bytes 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"CdnFile":

        bytes =Bytes .read (b )

        return CdnFile (bytes =bytes )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Bytes (self .bytes ))

        return b .getvalue ()
