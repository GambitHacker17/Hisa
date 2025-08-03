
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UserFull (TLObject ):
    """"""

    __slots__ :List [str ]=["id","settings","notify_settings","common_chats_count","blocked","phone_calls_available","phone_calls_private","can_pin_message","has_scheduled","video_calls_available","voice_messages_forbidden","translations_disabled","about","personal_photo","profile_photo","fallback_photo","bot_info","pinned_msg_id","folder_id","ttl_period","theme_emoticon","private_forward_name","bot_group_admin_rights","bot_broadcast_admin_rights","premium_gifts","wallpaper"]

    ID =0x93eadb53 
    QUALNAME ="types.UserFull"

    def __init__ (self ,*,id :int ,settings :"raw.base.PeerSettings",notify_settings :"raw.base.PeerNotifySettings",common_chats_count :int ,blocked :Optional [bool ]=None ,phone_calls_available :Optional [bool ]=None ,phone_calls_private :Optional [bool ]=None ,can_pin_message :Optional [bool ]=None ,has_scheduled :Optional [bool ]=None ,video_calls_available :Optional [bool ]=None ,voice_messages_forbidden :Optional [bool ]=None ,translations_disabled :Optional [bool ]=None ,about :Optional [str ]=None ,personal_photo :"raw.base.Photo"=None ,profile_photo :"raw.base.Photo"=None ,fallback_photo :"raw.base.Photo"=None ,bot_info :"raw.base.BotInfo"=None ,pinned_msg_id :Optional [int ]=None ,folder_id :Optional [int ]=None ,ttl_period :Optional [int ]=None ,theme_emoticon :Optional [str ]=None ,private_forward_name :Optional [str ]=None ,bot_group_admin_rights :"raw.base.ChatAdminRights"=None ,bot_broadcast_admin_rights :"raw.base.ChatAdminRights"=None ,premium_gifts :Optional [List ["raw.base.PremiumGiftOption"]]=None ,wallpaper :"raw.base.WallPaper"=None )->None :
        self .id =id 
        self .settings =settings 
        self .notify_settings =notify_settings 
        self .common_chats_count =common_chats_count 
        self .blocked =blocked 
        self .phone_calls_available =phone_calls_available 
        self .phone_calls_private =phone_calls_private 
        self .can_pin_message =can_pin_message 
        self .has_scheduled =has_scheduled 
        self .video_calls_available =video_calls_available 
        self .voice_messages_forbidden =voice_messages_forbidden 
        self .translations_disabled =translations_disabled 
        self .about =about 
        self .personal_photo =personal_photo 
        self .profile_photo =profile_photo 
        self .fallback_photo =fallback_photo 
        self .bot_info =bot_info 
        self .pinned_msg_id =pinned_msg_id 
        self .folder_id =folder_id 
        self .ttl_period =ttl_period 
        self .theme_emoticon =theme_emoticon 
        self .private_forward_name =private_forward_name 
        self .bot_group_admin_rights =bot_group_admin_rights 
        self .bot_broadcast_admin_rights =bot_broadcast_admin_rights 
        self .premium_gifts =premium_gifts 
        self .wallpaper =wallpaper 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UserFull":

        flags =Int .read (b )

        blocked =True if flags &(1 <<0 )else False 
        phone_calls_available =True if flags &(1 <<4 )else False 
        phone_calls_private =True if flags &(1 <<5 )else False 
        can_pin_message =True if flags &(1 <<7 )else False 
        has_scheduled =True if flags &(1 <<12 )else False 
        video_calls_available =True if flags &(1 <<13 )else False 
        voice_messages_forbidden =True if flags &(1 <<20 )else False 
        translations_disabled =True if flags &(1 <<23 )else False 
        id =Long .read (b )

        about =String .read (b )if flags &(1 <<1 )else None 
        settings =TLObject .read (b )

        personal_photo =TLObject .read (b )if flags &(1 <<21 )else None 

        profile_photo =TLObject .read (b )if flags &(1 <<2 )else None 

        fallback_photo =TLObject .read (b )if flags &(1 <<22 )else None 

        notify_settings =TLObject .read (b )

        bot_info =TLObject .read (b )if flags &(1 <<3 )else None 

        pinned_msg_id =Int .read (b )if flags &(1 <<6 )else None 
        common_chats_count =Int .read (b )

        folder_id =Int .read (b )if flags &(1 <<11 )else None 
        ttl_period =Int .read (b )if flags &(1 <<14 )else None 
        theme_emoticon =String .read (b )if flags &(1 <<15 )else None 
        private_forward_name =String .read (b )if flags &(1 <<16 )else None 
        bot_group_admin_rights =TLObject .read (b )if flags &(1 <<17 )else None 

        bot_broadcast_admin_rights =TLObject .read (b )if flags &(1 <<18 )else None 

        premium_gifts =TLObject .read (b )if flags &(1 <<19 )else []

        wallpaper =TLObject .read (b )if flags &(1 <<24 )else None 

        return UserFull (id =id ,settings =settings ,notify_settings =notify_settings ,common_chats_count =common_chats_count ,blocked =blocked ,phone_calls_available =phone_calls_available ,phone_calls_private =phone_calls_private ,can_pin_message =can_pin_message ,has_scheduled =has_scheduled ,video_calls_available =video_calls_available ,voice_messages_forbidden =voice_messages_forbidden ,translations_disabled =translations_disabled ,about =about ,personal_photo =personal_photo ,profile_photo =profile_photo ,fallback_photo =fallback_photo ,bot_info =bot_info ,pinned_msg_id =pinned_msg_id ,folder_id =folder_id ,ttl_period =ttl_period ,theme_emoticon =theme_emoticon ,private_forward_name =private_forward_name ,bot_group_admin_rights =bot_group_admin_rights ,bot_broadcast_admin_rights =bot_broadcast_admin_rights ,premium_gifts =premium_gifts ,wallpaper =wallpaper )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .blocked else 0 
        flags |=(1 <<4 )if self .phone_calls_available else 0 
        flags |=(1 <<5 )if self .phone_calls_private else 0 
        flags |=(1 <<7 )if self .can_pin_message else 0 
        flags |=(1 <<12 )if self .has_scheduled else 0 
        flags |=(1 <<13 )if self .video_calls_available else 0 
        flags |=(1 <<20 )if self .voice_messages_forbidden else 0 
        flags |=(1 <<23 )if self .translations_disabled else 0 
        flags |=(1 <<1 )if self .about is not None else 0 
        flags |=(1 <<21 )if self .personal_photo is not None else 0 
        flags |=(1 <<2 )if self .profile_photo is not None else 0 
        flags |=(1 <<22 )if self .fallback_photo is not None else 0 
        flags |=(1 <<3 )if self .bot_info is not None else 0 
        flags |=(1 <<6 )if self .pinned_msg_id is not None else 0 
        flags |=(1 <<11 )if self .folder_id is not None else 0 
        flags |=(1 <<14 )if self .ttl_period is not None else 0 
        flags |=(1 <<15 )if self .theme_emoticon is not None else 0 
        flags |=(1 <<16 )if self .private_forward_name is not None else 0 
        flags |=(1 <<17 )if self .bot_group_admin_rights is not None else 0 
        flags |=(1 <<18 )if self .bot_broadcast_admin_rights is not None else 0 
        flags |=(1 <<19 )if self .premium_gifts else 0 
        flags |=(1 <<24 )if self .wallpaper is not None else 0 
        b .write (Int (flags ))

        b .write (Long (self .id ))

        if self .about is not None :
            b .write (String (self .about ))

        b .write (self .settings .write ())

        if self .personal_photo is not None :
            b .write (self .personal_photo .write ())

        if self .profile_photo is not None :
            b .write (self .profile_photo .write ())

        if self .fallback_photo is not None :
            b .write (self .fallback_photo .write ())

        b .write (self .notify_settings .write ())

        if self .bot_info is not None :
            b .write (self .bot_info .write ())

        if self .pinned_msg_id is not None :
            b .write (Int (self .pinned_msg_id ))

        b .write (Int (self .common_chats_count ))

        if self .folder_id is not None :
            b .write (Int (self .folder_id ))

        if self .ttl_period is not None :
            b .write (Int (self .ttl_period ))

        if self .theme_emoticon is not None :
            b .write (String (self .theme_emoticon ))

        if self .private_forward_name is not None :
            b .write (String (self .private_forward_name ))

        if self .bot_group_admin_rights is not None :
            b .write (self .bot_group_admin_rights .write ())

        if self .bot_broadcast_admin_rights is not None :
            b .write (self .bot_broadcast_admin_rights .write ())

        if self .premium_gifts is not None :
            b .write (Vector (self .premium_gifts ))

        if self .wallpaper is not None :
            b .write (self .wallpaper .write ())

        return b .getvalue ()
