
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EditUserInfo (TLObject ):
    """"""

    __slots__ :List [str ]=["user_id","message","entities"]

    ID =0x66b91b70 
    QUALNAME ="functions.help.EditUserInfo"

    def __init__ (self ,*,user_id :"raw.base.InputUser",message :str ,entities :List ["raw.base.MessageEntity"])->None :
        self .user_id =user_id 
        self .message =message 
        self .entities =entities 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EditUserInfo":

        user_id =TLObject .read (b )

        message =String .read (b )

        entities =TLObject .read (b )

        return EditUserInfo (user_id =user_id ,message =message ,entities =entities )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .user_id .write ())

        b .write (String (self .message ))

        b .write (Vector (self .entities ))

        return b .getvalue ()
