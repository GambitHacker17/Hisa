
import logging 

import hisapyro 
from hisapyro import raw 

log =logging .getLogger (__name__ )

class GetPasswordHint :
    async def get_password_hint (
    self :"hisapyro.Client",
    )->str :
        """"""
        return (await self .invoke (raw .functions .account .GetPassword ())).hint 
