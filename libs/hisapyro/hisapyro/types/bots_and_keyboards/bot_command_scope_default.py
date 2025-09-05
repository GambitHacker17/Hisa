
import hisapyro 
from hisapyro import raw 
from .bot_command_scope import BotCommandScope 

class BotCommandScopeDefault (BotCommandScope ):
    """"""

    def __init__ (self ):
        super ().__init__ ("default")

    async def write (self ,client :"hisapyro.Client")->"raw.base.BotCommandScope":
        return raw .types .BotCommandScopeDefault ()
