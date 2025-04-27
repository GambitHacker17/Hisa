
from typing import Union 

import hisapyro 
from hisapyro import raw ,enums 

class SendChatAction :
    async def send_chat_action (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    action :"enums.ChatAction"
    )->bool :
        """"""

        action_name =action .name .lower ()

        if "upload"in action_name or "history"in action_name :
            action =action .value (progress =0 )
        else :
            action =action .value ()

        return await self .invoke (
        raw .functions .messages .SetTyping (
        peer =await self .resolve_peer (chat_id ),
        action =action 
        )
        )
