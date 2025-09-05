
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

DialogFilter =Union [raw .types .DialogFilter ,raw .types .DialogFilterChatlist ,raw .types .DialogFilterDefault ]

class DialogFilter :
    """"""

    QUALNAME ="hisapyro.raw.base.DialogFilter"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/dialog-filter")
