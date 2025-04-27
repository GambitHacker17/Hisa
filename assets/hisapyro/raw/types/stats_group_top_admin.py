
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class StatsGroupTopAdmin (TLObject ):
    """"""

    __slots__ :List [str ]=["user_id","deleted","kicked","banned"]

    ID =0xd7584c87 
    QUALNAME ="types.StatsGroupTopAdmin"

    def __init__ (self ,*,user_id :int ,deleted :int ,kicked :int ,banned :int )->None :
        self .user_id =user_id 
        self .deleted =deleted 
        self .kicked =kicked 
        self .banned =banned 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"StatsGroupTopAdmin":

        user_id =Long .read (b )

        deleted =Int .read (b )

        kicked =Int .read (b )

        banned =Int .read (b )

        return StatsGroupTopAdmin (user_id =user_id ,deleted =deleted ,kicked =kicked ,banned =banned )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .user_id ))

        b .write (Int (self .deleted ))

        b .write (Int (self .kicked ))

        b .write (Int (self .banned ))

        return b .getvalue ()
