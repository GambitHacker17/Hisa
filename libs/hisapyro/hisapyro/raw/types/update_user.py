
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateUser (TLObject ):
    """"""

    __slots__ :List [str ]=["user_id"]

    ID =0x20529438 
    QUALNAME ="types.UpdateUser"

    def __init__ (self ,*,user_id :int )->None :
        self .user_id =user_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateUser":

        user_id =Long .read (b )

        return UpdateUser (user_id =user_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .user_id ))

        return b .getvalue ()
