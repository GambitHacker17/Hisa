
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

InlineBotWebView =Union [raw .types .InlineBotWebView ]

class InlineBotWebView :
    """"""

    QUALNAME ="hisapyro.raw.base.InlineBotWebView"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/inline-bot-web-view")
