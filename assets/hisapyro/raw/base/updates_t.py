
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

Updates =Union [raw .types .UpdateShort ,raw .types .UpdateShortChatMessage ,raw .types .UpdateShortMessage ,raw .types .UpdateShortSentMessage ,raw .types .Updates ,raw .types .UpdatesCombined ,raw .types .UpdatesTooLong ]

class Updates :
    """"""

    QUALNAME ="hisapyro.raw.base.Updates"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/updates")
