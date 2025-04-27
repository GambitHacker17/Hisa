
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DhConfig (TLObject ):
    """"""

    __slots__ :List [str ]=["g","p","version","random"]

    ID =0x2c221edd 
    QUALNAME ="types.messages.DhConfig"

    def __init__ (self ,*,g :int ,p :bytes ,version :int ,random :bytes )->None :
        self .g =g 
        self .p =p 
        self .version =version 
        self .random =random 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DhConfig":

        g =Int .read (b )

        p =Bytes .read (b )

        version =Int .read (b )

        random =Bytes .read (b )

        return DhConfig (g =g ,p =p ,version =version ,random =random )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .g ))

        b .write (Bytes (self .p ))

        b .write (Int (self .version ))

        b .write (Bytes (self .random ))

        return b .getvalue ()
