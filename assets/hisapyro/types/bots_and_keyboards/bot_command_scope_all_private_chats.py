
import hisapyro 
from hisapyro import raw 
from .bot_command_scope import BotCommandScope 

class BotCommandScopeAllPrivateChats (BotCommandScope ):
    """"""

    def __init__ (self ):
        super ().__init__ ("all_private_chats")

    async def write (self ,client :"hisapyro.Client")->"raw.base.BotCommandScope":
        return raw .types .BotCommandScopeUsers ()
