
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputWebFileLocation (TLObject ):
    """"""

    __slots__ :List [str ]=["url","access_hash"]

    ID =0xc239d686 
    QUALNAME ="types.InputWebFileLocation"

    def __init__ (self ,*,url :str ,access_hash :int )->None :
        self .url =url 
        self .access_hash =access_hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputWebFileLocation":

        url =String .read (b )

        access_hash =Long .read (b )

        return InputWebFileLocation (url =url ,access_hash =access_hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .url ))

        b .write (Long (self .access_hash ))

        return b .getvalue ()
