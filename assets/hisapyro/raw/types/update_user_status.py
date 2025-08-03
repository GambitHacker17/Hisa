
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateUserStatus (TLObject ):
    """"""

    __slots__ :List [str ]=["user_id","status"]

    ID =0xe5bdf8de 
    QUALNAME ="types.UpdateUserStatus"

    def __init__ (self ,*,user_id :int ,status :"raw.base.UserStatus")->None :
        self .user_id =user_id 
        self .status =status 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateUserStatus":

        user_id =Long .read (b )

        status =TLObject .read (b )

        return UpdateUserStatus (user_id =user_id ,status =status )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .user_id ))

        b .write (self .status .write ())

        return b .getvalue ()
