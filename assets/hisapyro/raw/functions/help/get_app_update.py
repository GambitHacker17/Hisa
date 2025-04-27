
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetAppUpdate (TLObject ):
    """"""

    __slots__ :List [str ]=["source"]

    ID =0x522d5a7d 
    QUALNAME ="functions.help.GetAppUpdate"

    def __init__ (self ,*,source :str )->None :
        self .source =source 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetAppUpdate":

        source =String .read (b )

        return GetAppUpdate (source =source )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .source ))

        return b .getvalue ()
