
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

PostAddress =Union [raw .types .PostAddress ]

class PostAddress :
    """"""

    QUALNAME ="hisapyro.raw.base.PostAddress"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/post-address")
