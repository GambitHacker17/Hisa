
from typing import List ,Callable 

import hisapyro 
from hisapyro .filters import Filter 
from hisapyro .types import Message 
from .handler import Handler 

class DeletedMessagesHandler (Handler ):
    """"""

    def __init__ (self ,callback :Callable ,filters :Filter =None ):
        super ().__init__ (callback ,filters )

    async def check (self ,client :"hisapyro.Client",messages :List [Message ]):

        for message in messages :
            if await super ().check (client ,message ):
                return True 
        else :
            return False 
