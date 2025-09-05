
import hisapyro 
from hisapyro import raw 
from ..object import Object 

class BotCommandScope (Object ):
    """"""

    def __init__ (self ,type :str ):
        super ().__init__ ()

        self .type =type 

    async def write (self ,client :"hisapyro.Client")->"raw.base.BotCommandScope":
        raise NotImplementedError 
