
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetDeepLinkInfo (TLObject ):
    """"""

    __slots__ :List [str ]=["path"]

    ID =0x3fedc75f 
    QUALNAME ="functions.help.GetDeepLinkInfo"

    def __init__ (self ,*,path :str )->None :
        self .path =path 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetDeepLinkInfo":

        path =String .read (b )

        return GetDeepLinkInfo (path =path )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .path ))

        return b .getvalue ()
