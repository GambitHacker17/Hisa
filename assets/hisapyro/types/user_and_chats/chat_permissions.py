
from hisapyro import raw 
from ..object import Object 

class ChatPermissions (Object ):
    """"""

    def __init__ (
    self ,
    *,
    can_send_messages :bool =None ,
    can_send_media_messages :bool =None ,
    can_send_other_messages :bool =None ,
    can_send_polls :bool =None ,
    can_add_web_page_previews :bool =None ,
    can_change_info :bool =None ,
    can_invite_users :bool =None ,
    can_pin_messages :bool =None 
    ):
        super ().__init__ (None )

        self .can_send_messages =can_send_messages 
        self .can_send_media_messages =can_send_media_messages 
        self .can_send_other_messages =can_send_other_messages 
        self .can_send_polls =can_send_polls 
        self .can_add_web_page_previews =can_add_web_page_previews 
        self .can_change_info =can_change_info 
        self .can_invite_users =can_invite_users 
        self .can_pin_messages =can_pin_messages 

    @staticmethod 
    def _parse (denied_permissions :"raw.base.ChatBannedRights")->"ChatPermissions":
        if isinstance (denied_permissions ,raw .types .ChatBannedRights ):
            return ChatPermissions (
            can_send_messages =not denied_permissions .send_messages ,
            can_send_media_messages =not denied_permissions .send_media ,
            can_send_other_messages =any ([
            not denied_permissions .send_stickers ,
            not denied_permissions .send_gifs ,
            not denied_permissions .send_games ,
            not denied_permissions .send_inline 
            ]),
            can_add_web_page_previews =not denied_permissions .embed_links ,
            can_send_polls =not denied_permissions .send_polls ,
            can_change_info =not denied_permissions .change_info ,
            can_invite_users =not denied_permissions .invite_users ,
            can_pin_messages =not denied_permissions .pin_messages 
            )
