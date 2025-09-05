
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageMediaGame (TLObject ):
    """"""

    __slots__ :List [str ]=["game"]

    ID =0xfdb19008 
    QUALNAME ="types.MessageMediaGame"

    def __init__ (self ,*,game :"raw.base.Game")->None :
        self .game =game 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageMediaGame":

        game =TLObject .read (b )

        return MessageMediaGame (game =game )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .game .write ())

        return b .getvalue ()
