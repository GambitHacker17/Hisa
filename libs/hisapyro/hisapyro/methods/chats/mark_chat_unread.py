
from typing import Union 

import hisapyro 
from hisapyro import raw 

class MarkChatUnread :
    async def mark_chat_unread (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    )->bool :
        """"""

        return await self .invoke (
        raw .functions .messages .MarkDialogUnread (
        peer =await self .resolve_peer (chat_id ),
        unread =True 
        )
        )
