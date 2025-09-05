
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetTopReactions (TLObject ):
    """"""

    __slots__ :List [str ]=["limit","hash"]

    ID =0xbb8125ba 
    QUALNAME ="functions.messages.GetTopReactions"

    def __init__ (self ,*,limit :int ,hash :int )->None :
        self .limit =limit 
        self .hash =hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetTopReactions":

        limit =Int .read (b )

        hash =Long .read (b )

        return GetTopReactions (limit =limit ,hash =hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .limit ))

        b .write (Long (self .hash ))

        return b .getvalue ()
