
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

BotInlineMessage =Union [raw .types .BotInlineMessageMediaAuto ,raw .types .BotInlineMessageMediaContact ,raw .types .BotInlineMessageMediaGeo ,raw .types .BotInlineMessageMediaInvoice ,raw .types .BotInlineMessageMediaVenue ,raw .types .BotInlineMessageText ]

class BotInlineMessage :
    """"""

    QUALNAME ="hisapyro.raw.base.BotInlineMessage"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/bot-inline-message")
