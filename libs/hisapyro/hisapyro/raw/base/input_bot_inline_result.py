
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

InputBotInlineResult =Union [raw .types .InputBotInlineResult ,raw .types .InputBotInlineResultDocument ,raw .types .InputBotInlineResultGame ,raw .types .InputBotInlineResultPhoto ]

class InputBotInlineResult :
    """"""

    QUALNAME ="hisapyro.raw.base.InputBotInlineResult"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/input-bot-inline-result")
