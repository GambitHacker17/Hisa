
from typing import Union ,Optional 

import hisapyro 
from hisapyro import raw 

class SetSlowMode :
    async def set_slow_mode (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    seconds :Optional [int ]
    )->bool :
        """"""

        await self .invoke (
        raw .functions .channels .ToggleSlowMode (
        channel =await self .resolve_peer (chat_id ),
        seconds =seconds or 0 
        )
        )

        return True 
