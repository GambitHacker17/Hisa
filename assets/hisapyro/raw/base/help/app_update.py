
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

AppUpdate =Union [raw .types .help .AppUpdate ,raw .types .help .NoAppUpdate ]

class AppUpdate :
    """"""

    QUALNAME ="hisapyro.raw.base.help.AppUpdate"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/app-update")
