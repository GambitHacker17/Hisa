
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class CdnConfig (TLObject ):
    """"""

    __slots__ :List [str ]=["public_keys"]

    ID =0x5725e40a 
    QUALNAME ="types.CdnConfig"

    def __init__ (self ,*,public_keys :List ["raw.base.CdnPublicKey"])->None :
        self .public_keys =public_keys 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"CdnConfig":

        public_keys =TLObject .read (b )

        return CdnConfig (public_keys =public_keys )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .public_keys ))

        return b .getvalue ()
