
from typing import Union 

import hisapyro 
from hisapyro import raw 
from .bot_command_scope import BotCommandScope 

class BotCommandScopeChat (BotCommandScope ):
    """"""

    def __init__ (self ,chat_id :Union [int ,str ]):
        super ().__init__ ("chat")

        self .chat_id =chat_id 

    async def write (self ,client :"hisapyro.Client")->"raw.base.BotCommandScope":
        return raw .types .BotCommandScopePeer (
        peer =await client .resolve_peer (self .chat_id )
        )
