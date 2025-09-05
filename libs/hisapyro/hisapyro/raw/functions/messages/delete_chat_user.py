
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DeleteChatUser (TLObject ):
    """"""

    __slots__ :List [str ]=["chat_id","user_id","revoke_history"]

    ID =0xa2185cab 
    QUALNAME ="functions.messages.DeleteChatUser"

    def __init__ (self ,*,chat_id :int ,user_id :"raw.base.InputUser",revoke_history :Optional [bool ]=None )->None :
        self .chat_id =chat_id 
        self .user_id =user_id 
        self .revoke_history =revoke_history 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DeleteChatUser":

        flags =Int .read (b )

        revoke_history =True if flags &(1 <<0 )else False 
        chat_id =Long .read (b )

        user_id =TLObject .read (b )

        return DeleteChatUser (chat_id =chat_id ,user_id =user_id ,revoke_history =revoke_history )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .revoke_history else 0 
        b .write (Int (flags ))

        b .write (Long (self .chat_id ))

        b .write (self .user_id .write ())

        return b .getvalue ()
