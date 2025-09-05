
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class HighScore (TLObject ):
    """"""

    __slots__ :List [str ]=["pos","user_id","score"]

    ID =0x73a379eb 
    QUALNAME ="types.HighScore"

    def __init__ (self ,*,pos :int ,user_id :int ,score :int )->None :
        self .pos =pos 
        self .user_id =user_id 
        self .score =score 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"HighScore":

        pos =Int .read (b )

        user_id =Long .read (b )

        score =Int .read (b )

        return HighScore (pos =pos ,user_id =user_id ,score =score )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .pos ))

        b .write (Long (self .user_id ))

        b .write (Int (self .score ))

        return b .getvalue ()
