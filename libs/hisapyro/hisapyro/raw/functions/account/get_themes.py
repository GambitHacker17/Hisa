
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetThemes (TLObject ):
    """"""

    __slots__ :List [str ]=["format","hash"]

    ID =0x7206e458 
    QUALNAME ="functions.account.GetThemes"

    def __init__ (self ,*,format :str ,hash :int )->None :
        self .format =format 
        self .hash =hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetThemes":

        format =String .read (b )

        hash =Long .read (b )

        return GetThemes (format =format ,hash =hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .format ))

        b .write (Long (self .hash ))

        return b .getvalue ()
