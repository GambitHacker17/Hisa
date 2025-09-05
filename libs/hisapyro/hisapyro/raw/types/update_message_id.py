
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateMessageID (TLObject ):
    """"""

    __slots__ :List [str ]=["id","random_id"]

    ID =0x4e90bfd6 
    QUALNAME ="types.UpdateMessageID"

    def __init__ (self ,*,id :int ,random_id :int )->None :
        self .id =id 
        self .random_id =random_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateMessageID":

        id =Int .read (b )

        random_id =Long .read (b )

        return UpdateMessageID (id =id ,random_id =random_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .id ))

        b .write (Long (self .random_id ))

        return b .getvalue ()
