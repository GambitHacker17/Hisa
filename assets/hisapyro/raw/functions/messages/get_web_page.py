
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetWebPage (TLObject ):
    """"""

    __slots__ :List [str ]=["url","hash"]

    ID =0x32ca8f91 
    QUALNAME ="functions.messages.GetWebPage"

    def __init__ (self ,*,url :str ,hash :int )->None :
        self .url =url 
        self .hash =hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetWebPage":

        url =String .read (b )

        hash =Int .read (b )

        return GetWebPage (url =url ,hash =hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .url ))

        b .write (Int (self .hash ))

        return b .getvalue ()
