
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AppConfig (TLObject ):
    """"""

    __slots__ :List [str ]=["hash","config"]

    ID =0xdd18782e 
    QUALNAME ="types.help.AppConfig"

    def __init__ (self ,*,hash :int ,config :"raw.base.JSONValue")->None :
        self .hash =hash 
        self .config =config 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AppConfig":

        hash =Int .read (b )

        config =TLObject .read (b )

        return AppConfig (hash =hash ,config =config )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .hash ))

        b .write (self .config .write ())

        return b .getvalue ()
