
import logging 

import hisapyro 
from hisapyro import raw 

log =logging .getLogger (__name__ )

class LogOut :
    async def log_out (
    self :"hisapyro.Client",
    ):
        """"""
        await self .invoke (raw .functions .auth .LogOut ())
        await self .stop ()
        await self .storage .delete ()

        return True 
