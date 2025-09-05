
from typing import List 

import hisapyro 
from hisapyro import raw 
from hisapyro import types 

class ImportContacts :
    async def import_contacts (
    self :"hisapyro.Client",
    contacts :List ["types.InputPhoneContact"]
    ):
        """"""
        imported_contacts =await self .invoke (
        raw .functions .contacts .ImportContacts (
        contacts =contacts 
        )
        )

        return imported_contacts 
