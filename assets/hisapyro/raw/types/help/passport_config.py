
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PassportConfig (TLObject ):
    """"""

    __slots__ :List [str ]=["hash","countries_langs"]

    ID =0xa098d6af 
    QUALNAME ="types.help.PassportConfig"

    def __init__ (self ,*,hash :int ,countries_langs :"raw.base.DataJSON")->None :
        self .hash =hash 
        self .countries_langs =countries_langs 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PassportConfig":

        hash =Int .read (b )

        countries_langs =TLObject .read (b )

        return PassportConfig (hash =hash ,countries_langs =countries_langs )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .hash ))

        b .write (self .countries_langs .write ())

        return b .getvalue ()
