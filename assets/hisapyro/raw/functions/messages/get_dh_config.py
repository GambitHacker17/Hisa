
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetDhConfig (TLObject ):
    """"""

    __slots__ :List [str ]=["version","random_length"]

    ID =0x26cf8950 
    QUALNAME ="functions.messages.GetDhConfig"

    def __init__ (self ,*,version :int ,random_length :int )->None :
        self .version =version 
        self .random_length =random_length 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetDhConfig":

        version =Int .read (b )

        random_length =Int .read (b )

        return GetDhConfig (version =version ,random_length =random_length )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .version ))

        b .write (Int (self .random_length ))

        return b .getvalue ()
