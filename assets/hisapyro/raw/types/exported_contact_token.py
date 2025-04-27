
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ExportedContactToken (TLObject ):
    """"""

    __slots__ :List [str ]=["url","expires"]

    ID =0x41bf109b 
    QUALNAME ="types.ExportedContactToken"

    def __init__ (self ,*,url :str ,expires :int )->None :
        self .url =url 
        self .expires =expires 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ExportedContactToken":

        url =String .read (b )

        expires =Int .read (b )

        return ExportedContactToken (url =url ,expires =expires )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .url ))

        b .write (Int (self .expires ))

        return b .getvalue ()
