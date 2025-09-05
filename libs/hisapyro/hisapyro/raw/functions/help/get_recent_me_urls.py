
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetRecentMeUrls (TLObject ):
    """"""

    __slots__ :List [str ]=["referer"]

    ID =0x3dc0f114 
    QUALNAME ="functions.help.GetRecentMeUrls"

    def __init__ (self ,*,referer :str )->None :
        self .referer =referer 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetRecentMeUrls":

        referer =String .read (b )

        return GetRecentMeUrls (referer =referer )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .referer ))

        return b .getvalue ()
