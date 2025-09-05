
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateUserTyping (TLObject ):
    """"""

    __slots__ :List [str ]=["user_id","action"]

    ID =0xc01e857f 
    QUALNAME ="types.UpdateUserTyping"

    def __init__ (self ,*,user_id :int ,action :"raw.base.SendMessageAction")->None :
        self .user_id =user_id 
        self .action =action 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateUserTyping":

        user_id =Long .read (b )

        action =TLObject .read (b )

        return UpdateUserTyping (user_id =user_id ,action =action )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .user_id ))

        b .write (self .action .write ())

        return b .getvalue ()
