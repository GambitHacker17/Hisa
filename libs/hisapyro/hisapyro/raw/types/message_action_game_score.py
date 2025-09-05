
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageActionGameScore (TLObject ):
    """"""

    __slots__ :List [str ]=["game_id","score"]

    ID =0x92a72876 
    QUALNAME ="types.MessageActionGameScore"

    def __init__ (self ,*,game_id :int ,score :int )->None :
        self .game_id =game_id 
        self .score =score 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageActionGameScore":

        game_id =Long .read (b )

        score =Int .read (b )

        return MessageActionGameScore (game_id =game_id ,score =score )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .game_id ))

        b .write (Int (self .score ))

        return b .getvalue ()
