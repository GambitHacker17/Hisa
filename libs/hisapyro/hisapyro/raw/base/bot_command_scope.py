
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

BotCommandScope =Union [raw .types .BotCommandScopeChatAdmins ,raw .types .BotCommandScopeChats ,raw .types .BotCommandScopeDefault ,raw .types .BotCommandScopePeer ,raw .types .BotCommandScopePeerAdmins ,raw .types .BotCommandScopePeerUser ,raw .types .BotCommandScopeUsers ]

class BotCommandScope :
    """"""

    QUALNAME ="hisapyro.raw.base.BotCommandScope"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/bot-command-scope")
