
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class CdnPublicKey (TLObject ):
    """"""

    __slots__ :List [str ]=["dc_id","public_key"]

    ID =0xc982eaba 
    QUALNAME ="types.CdnPublicKey"

    def __init__ (self ,*,dc_id :int ,public_key :str )->None :
        self .dc_id =dc_id 
        self .public_key =public_key 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"CdnPublicKey":

        dc_id =Int .read (b )

        public_key =String .read (b )

        return CdnPublicKey (dc_id =dc_id ,public_key =public_key )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .dc_id ))

        b .write (String (self .public_key ))

        return b .getvalue ()
