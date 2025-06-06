
from typing import Union 

import hisapyro 
from hisapyro import raw 

class DeleteUserHistory :
    async def delete_user_history (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    user_id :Union [int ,str ],
    )->bool :
        """"""

        r =await self .invoke (
        raw .functions .channels .DeleteParticipantHistory (
        channel =await self .resolve_peer (chat_id ),
        participant =await self .resolve_peer (user_id )
        )
        )

        return bool (r .pts_count )
