
from typing import Union 

import hisapyro 
from hisapyro import raw 

class DeleteChatInviteLink :
    async def delete_chat_invite_link (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    invite_link :str ,
    )->bool :
        """"""

        return await self .invoke (
        raw .functions .messages .DeleteExportedChatInvite (
        peer =await self .resolve_peer (chat_id ),
        link =invite_link ,
        )
        )
