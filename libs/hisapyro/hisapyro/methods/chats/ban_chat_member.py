
from datetime import datetime 
from typing import Union 

import hisapyro 
from hisapyro import raw ,utils 
from hisapyro import types 

class BanChatMember :
    async def ban_chat_member (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    user_id :Union [int ,str ],
    until_date :datetime =utils .zero_datetime ()
    )->Union ["types.Message",bool ]:
        """"""
        chat_peer =await self .resolve_peer (chat_id )
        user_peer =await self .resolve_peer (user_id )

        if isinstance (chat_peer ,raw .types .InputPeerChannel ):
            r =await self .invoke (
            raw .functions .channels .EditBanned (
            channel =chat_peer ,
            participant =user_peer ,
            banned_rights =raw .types .ChatBannedRights (
            until_date =utils .datetime_to_timestamp (until_date ),
            view_messages =True ,
            send_messages =True ,
            send_media =True ,
            send_stickers =True ,
            send_gifs =True ,
            send_games =True ,
            send_inline =True ,
            embed_links =True 
            )
            )
            )
        else :
            r =await self .invoke (
            raw .functions .messages .DeleteChatUser (
            chat_id =abs (chat_id ),
            user_id =user_peer 
            )
            )

        for i in r .updates :
            if isinstance (i ,(raw .types .UpdateNewMessage ,raw .types .UpdateNewChannelMessage )):
                return await types .Message ._parse (
                self ,i .message ,
                {i .id :i for i in r .users },
                {i .id :i for i in r .chats }
                )
        else :
            return True 
