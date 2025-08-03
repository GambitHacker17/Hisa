
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChatAdminRights (TLObject ):
    """"""

    __slots__ :List [str ]=["change_info","post_messages","edit_messages","delete_messages","ban_users","invite_users","pin_messages","add_admins","anonymous","manage_call","other","manage_topics"]

    ID =0x5fb224d5 
    QUALNAME ="types.ChatAdminRights"

    def __init__ (self ,*,change_info :Optional [bool ]=None ,post_messages :Optional [bool ]=None ,edit_messages :Optional [bool ]=None ,delete_messages :Optional [bool ]=None ,ban_users :Optional [bool ]=None ,invite_users :Optional [bool ]=None ,pin_messages :Optional [bool ]=None ,add_admins :Optional [bool ]=None ,anonymous :Optional [bool ]=None ,manage_call :Optional [bool ]=None ,other :Optional [bool ]=None ,manage_topics :Optional [bool ]=None )->None :
        self .change_info =change_info 
        self .post_messages =post_messages 
        self .edit_messages =edit_messages 
        self .delete_messages =delete_messages 
        self .ban_users =ban_users 
        self .invite_users =invite_users 
        self .pin_messages =pin_messages 
        self .add_admins =add_admins 
        self .anonymous =anonymous 
        self .manage_call =manage_call 
        self .other =other 
        self .manage_topics =manage_topics 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChatAdminRights":

        flags =Int .read (b )

        change_info =True if flags &(1 <<0 )else False 
        post_messages =True if flags &(1 <<1 )else False 
        edit_messages =True if flags &(1 <<2 )else False 
        delete_messages =True if flags &(1 <<3 )else False 
        ban_users =True if flags &(1 <<4 )else False 
        invite_users =True if flags &(1 <<5 )else False 
        pin_messages =True if flags &(1 <<7 )else False 
        add_admins =True if flags &(1 <<9 )else False 
        anonymous =True if flags &(1 <<10 )else False 
        manage_call =True if flags &(1 <<11 )else False 
        other =True if flags &(1 <<12 )else False 
        manage_topics =True if flags &(1 <<13 )else False 
        return ChatAdminRights (change_info =change_info ,post_messages =post_messages ,edit_messages =edit_messages ,delete_messages =delete_messages ,ban_users =ban_users ,invite_users =invite_users ,pin_messages =pin_messages ,add_admins =add_admins ,anonymous =anonymous ,manage_call =manage_call ,other =other ,manage_topics =manage_topics )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .change_info else 0 
        flags |=(1 <<1 )if self .post_messages else 0 
        flags |=(1 <<2 )if self .edit_messages else 0 
        flags |=(1 <<3 )if self .delete_messages else 0 
        flags |=(1 <<4 )if self .ban_users else 0 
        flags |=(1 <<5 )if self .invite_users else 0 
        flags |=(1 <<7 )if self .pin_messages else 0 
        flags |=(1 <<9 )if self .add_admins else 0 
        flags |=(1 <<10 )if self .anonymous else 0 
        flags |=(1 <<11 )if self .manage_call else 0 
        flags |=(1 <<12 )if self .other else 0 
        flags |=(1 <<13 )if self .manage_topics else 0 
        b .write (Int (flags ))

        return b .getvalue ()
