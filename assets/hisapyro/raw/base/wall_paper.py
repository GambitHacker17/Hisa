
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

WallPaper =Union [raw .types .WallPaper ,raw .types .WallPaperNoFile ]

class WallPaper :
    """"""

    QUALNAME ="hisapyro.raw.base.WallPaper"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/wall-paper")
