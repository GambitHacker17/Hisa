
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ReactionEmoji (TLObject ):
    """"""

    __slots__ :List [str ]=["emoticon"]

    ID =0x1b2286b8 
    QUALNAME ="types.ReactionEmoji"

    def __init__ (self ,*,emoticon :str )->None :
        self .emoticon =emoticon 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ReactionEmoji":

        emoticon =String .read (b )

        return ReactionEmoji (emoticon =emoticon )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .emoticon ))

        return b .getvalue ()
