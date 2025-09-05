
import hisapyro 
from hisapyro import raw 

class GetContactsCount :
    async def get_contacts_count (
    self :"hisapyro.Client"
    )->int :
        """"""

        return len ((await self .invoke (raw .functions .contacts .GetContacts (hash =0 ))).contacts )
