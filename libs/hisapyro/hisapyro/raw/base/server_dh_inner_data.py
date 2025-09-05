
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

ServerDHInnerData =Union [raw .types .ServerDHInnerData ]

class ServerDHInnerData :
    """"""

    QUALNAME ="hisapyro.raw.base.ServerDHInnerData"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/server-dh-inner-data")
