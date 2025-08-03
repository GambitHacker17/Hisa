
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetAppChangelog (TLObject ):
    """"""

    __slots__ :List [str ]=["prev_app_version"]

    ID =0x9010ef6f 
    QUALNAME ="functions.help.GetAppChangelog"

    def __init__ (self ,*,prev_app_version :str )->None :
        self .prev_app_version =prev_app_version 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetAppChangelog":

        prev_app_version =String .read (b )

        return GetAppChangelog (prev_app_version =prev_app_version )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .prev_app_version ))

        return b .getvalue ()
