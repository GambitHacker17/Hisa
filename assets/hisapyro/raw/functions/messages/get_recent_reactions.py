
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetRecentReactions (TLObject ):
    """"""

    __slots__ :List [str ]=["limit","hash"]

    ID =0x39461db2 
    QUALNAME ="functions.messages.GetRecentReactions"

    def __init__ (self ,*,limit :int ,hash :int )->None :
        self .limit =limit 
        self .hash =hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetRecentReactions":

        limit =Int .read (b )

        hash =Long .read (b )

        return GetRecentReactions (limit =limit ,hash =hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .limit ))

        b .write (Long (self .hash ))

        return b .getvalue ()
