
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

SavedGifs =Union [raw .types .messages .SavedGifs ,raw .types .messages .SavedGifsNotModified ]

class SavedGifs :
    """"""

    QUALNAME ="hisapyro.raw.base.messages.SavedGifs"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/saved-gifs")
