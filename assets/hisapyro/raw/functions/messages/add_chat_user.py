
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AddChatUser (TLObject ):
    """"""

    __slots__ :List [str ]=["chat_id","user_id","fwd_limit"]

    ID =0xf24753e3 
    QUALNAME ="functions.messages.AddChatUser"

    def __init__ (self ,*,chat_id :int ,user_id :"raw.base.InputUser",fwd_limit :int )->None :
        self .chat_id =chat_id 
        self .user_id =user_id 
        self .fwd_limit =fwd_limit 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AddChatUser":

        chat_id =Long .read (b )

        user_id =TLObject .read (b )

        fwd_limit =Int .read (b )

        return AddChatUser (chat_id =chat_id ,user_id =user_id ,fwd_limit =fwd_limit )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .chat_id ))

        b .write (self .user_id .write ())

        b .write (Int (self .fwd_limit ))

        return b .getvalue ()
