
from typing import Union 

import hisapyro 
from hisapyro import raw 

class UnblockUser :
    async def unblock_user (
    self :"hisapyro.Client",
    user_id :Union [int ,str ]
    )->bool :
        """"""
        return bool (
        await self .invoke (
        raw .functions .contacts .Unblock (
        id =await self .resolve_peer (user_id )
        )
        )
        )
