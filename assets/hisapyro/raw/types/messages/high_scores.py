
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class HighScores (TLObject ):
    """"""

    __slots__ :List [str ]=["scores","users"]

    ID =0x9a3bfd99 
    QUALNAME ="types.messages.HighScores"

    def __init__ (self ,*,scores :List ["raw.base.HighScore"],users :List ["raw.base.User"])->None :
        self .scores =scores 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"HighScores":

        scores =TLObject .read (b )

        users =TLObject .read (b )

        return HighScores (scores =scores ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .scores ))

        b .write (Vector (self .users ))

        return b .getvalue ()
