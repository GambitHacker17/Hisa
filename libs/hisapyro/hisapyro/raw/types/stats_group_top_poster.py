
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class StatsGroupTopPoster (TLObject ):
    """"""

    __slots__ :List [str ]=["user_id","messages","avg_chars"]

    ID =0x9d04af9b 
    QUALNAME ="types.StatsGroupTopPoster"

    def __init__ (self ,*,user_id :int ,messages :int ,avg_chars :int )->None :
        self .user_id =user_id 
        self .messages =messages 
        self .avg_chars =avg_chars 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"StatsGroupTopPoster":

        user_id =Long .read (b )

        messages =Int .read (b )

        avg_chars =Int .read (b )

        return StatsGroupTopPoster (user_id =user_id ,messages =messages ,avg_chars =avg_chars )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .user_id ))

        b .write (Int (self .messages ))

        b .write (Int (self .avg_chars ))

        return b .getvalue ()
