
import logging 
from typing import Union 

import hisapyro 
from hisapyro import raw 
from hisapyro import types 

log =logging .getLogger (__name__ )

class SignIn :
    async def sign_in (
    self :"hisapyro.Client",
    phone_number :str ,
    phone_code_hash :str ,
    phone_code :str 
    )->Union ["types.User","types.TermsOfService",bool ]:
        """"""
        phone_number =phone_number .strip (" +")

        r =await self .invoke (
        raw .functions .auth .SignIn (
        phone_number =phone_number ,
        phone_code_hash =phone_code_hash ,
        phone_code =phone_code 
        )
        )

        if isinstance (r ,raw .types .auth .AuthorizationSignUpRequired ):
            if r .terms_of_service :
                return types .TermsOfService ._parse (terms_of_service =r .terms_of_service )

            return False 
        else :
            await self .storage .user_id (r .user .id )
            await self .storage .is_bot (False )

            return types .User ._parse (self ,r .user )
