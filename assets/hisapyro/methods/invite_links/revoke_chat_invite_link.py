
from typing import Union 

import hisapyro 
from hisapyro import raw 
from hisapyro import types 

class RevokeChatInviteLink :
    async def revoke_chat_invite_link (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    invite_link :str ,
    )->"types.ChatInviteLink":
        """"""

        r =await self .invoke (
        raw .functions .messages .EditExportedChatInvite (
        peer =await self .resolve_peer (chat_id ),
        link =invite_link ,
        revoked =True 
        )
        )

        users ={i .id :i for i in r .users }

        chat_invite =(
        r .new_invite 
        if isinstance (r ,raw .types .messages .ExportedChatInviteReplaced )
        else r .invite 
        )

        return types .ChatInviteLink ._parse (self ,chat_invite ,users )
