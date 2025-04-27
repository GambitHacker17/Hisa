
from typing import Optional 

import hisapyro 
from hisapyro import raw 

class SetUsername :
    async def set_username (
    self :"hisapyro.Client",
    username :Optional [str ]
    )->bool :
        """"""

        return bool (
        await self .invoke (
        raw .functions .account .UpdateUsername (
        username =username or ""
        )
        )
        )
