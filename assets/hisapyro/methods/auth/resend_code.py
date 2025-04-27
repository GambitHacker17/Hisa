
import logging 

import hisapyro 
from hisapyro import raw 
from hisapyro import types 

log =logging .getLogger (__name__ )

class ResendCode :
    async def resend_code (
    self :"hisapyro.Client",
    phone_number :str ,
    phone_code_hash :str 
    )->"types.SentCode":
        """"""
        phone_number =phone_number .strip (" +")

        r =await self .invoke (
        raw .functions .auth .ResendCode (
        phone_number =phone_number ,
        phone_code_hash =phone_code_hash 
        )
        )

        return types .SentCode ._parse (r )
