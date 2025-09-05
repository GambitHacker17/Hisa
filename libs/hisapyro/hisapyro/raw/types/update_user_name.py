
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateUserName (TLObject ):
    """"""

    __slots__ :List [str ]=["user_id","first_name","last_name","usernames"]

    ID =0xa7848924 
    QUALNAME ="types.UpdateUserName"

    def __init__ (self ,*,user_id :int ,first_name :str ,last_name :str ,usernames :List ["raw.base.Username"])->None :
        self .user_id =user_id 
        self .first_name =first_name 
        self .last_name =last_name 
        self .usernames =usernames 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateUserName":

        user_id =Long .read (b )

        first_name =String .read (b )

        last_name =String .read (b )

        usernames =TLObject .read (b )

        return UpdateUserName (user_id =user_id ,first_name =first_name ,last_name =last_name ,usernames =usernames )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .user_id ))

        b .write (String (self .first_name ))

        b .write (String (self .last_name ))

        b .write (Vector (self .usernames ))

        return b .getvalue ()
