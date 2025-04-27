
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateUserPhone (TLObject ):
    """"""

    __slots__ :List [str ]=["user_id","phone"]

    ID =0x5492a13 
    QUALNAME ="types.UpdateUserPhone"

    def __init__ (self ,*,user_id :int ,phone :str )->None :
        self .user_id =user_id 
        self .phone =phone 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateUserPhone":

        user_id =Long .read (b )

        phone =String .read (b )

        return UpdateUserPhone (user_id =user_id ,phone =phone )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .user_id ))

        b .write (String (self .phone ))

        return b .getvalue ()
