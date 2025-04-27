
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateBotStopped (TLObject ):
    """"""

    __slots__ :List [str ]=["user_id","date","stopped","qts"]

    ID =0xc4870a49 
    QUALNAME ="types.UpdateBotStopped"

    def __init__ (self ,*,user_id :int ,date :int ,stopped :bool ,qts :int )->None :
        self .user_id =user_id 
        self .date =date 
        self .stopped =stopped 
        self .qts =qts 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateBotStopped":

        user_id =Long .read (b )

        date =Int .read (b )

        stopped =Bool .read (b )

        qts =Int .read (b )

        return UpdateBotStopped (user_id =user_id ,date =date ,stopped =stopped ,qts =qts )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .user_id ))

        b .write (Int (self .date ))

        b .write (Bool (self .stopped ))

        b .write (Int (self .qts ))

        return b .getvalue ()
