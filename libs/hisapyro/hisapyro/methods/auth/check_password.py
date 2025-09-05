
import logging 

import hisapyro 
from hisapyro import raw 
from hisapyro import types 
from hisapyro .utils import compute_password_check 

log =logging .getLogger (__name__ )

class CheckPassword :
    async def check_password (
    self :"hisapyro.Client",
    password :str 
    )->"types.User":
        """"""
        r =await self .invoke (
        raw .functions .auth .CheckPassword (
        password =compute_password_check (
        await self .invoke (raw .functions .account .GetPassword ()),
        password 
        )
        )
        )

        await self .storage .user_id (r .user .id )
        await self .storage .is_bot (False )

        return types .User ._parse (self ,r .user )
