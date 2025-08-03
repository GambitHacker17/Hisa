
from typing import Union 

import hisapyro 
from hisapyro import raw 
from hisapyro import types 

class ExportChatInviteLink :
    async def export_chat_invite_link (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    )->"types.ChatInviteLink":
        """"""
        r =await self .invoke (
        raw .functions .messages .ExportChatInvite (
        peer =await self .resolve_peer (chat_id ),
        legacy_revoke_permanent =True 
        )
        )

        return r .link 
