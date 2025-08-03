
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetStickers (TLObject ):
    """"""

    __slots__ :List [str ]=["emoticon","hash"]

    ID =0xd5a5d3a1 
    QUALNAME ="functions.messages.GetStickers"

    def __init__ (self ,*,emoticon :str ,hash :int )->None :
        self .emoticon =emoticon 
        self .hash =hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetStickers":

        emoticon =String .read (b )

        hash =Long .read (b )

        return GetStickers (emoticon =emoticon ,hash =hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .emoticon ))

        b .write (Long (self .hash ))

        return b .getvalue ()
