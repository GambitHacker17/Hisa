
from typing import Union 

import hisapyro 
from hisapyro import raw 

class DeleteSupergroup :
    async def delete_supergroup (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ]
    )->bool :
        """"""
        await self .invoke (
        raw .functions .channels .DeleteChannel (
        channel =await self .resolve_peer (chat_id )
        )
        )

        return True 
