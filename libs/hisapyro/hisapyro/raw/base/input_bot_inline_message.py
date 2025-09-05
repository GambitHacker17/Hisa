
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

InputBotInlineMessage =Union [raw .types .InputBotInlineMessageGame ,raw .types .InputBotInlineMessageMediaAuto ,raw .types .InputBotInlineMessageMediaContact ,raw .types .InputBotInlineMessageMediaGeo ,raw .types .InputBotInlineMessageMediaInvoice ,raw .types .InputBotInlineMessageMediaVenue ,raw .types .InputBotInlineMessageText ]

class InputBotInlineMessage :
    """"""

    QUALNAME ="hisapyro.raw.base.InputBotInlineMessage"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/input-bot-inline-message")
