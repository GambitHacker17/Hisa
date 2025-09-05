
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

PhotoSize =Union [raw .types .PhotoCachedSize ,raw .types .PhotoPathSize ,raw .types .PhotoSize ,raw .types .PhotoSizeEmpty ,raw .types .PhotoSizeProgressive ,raw .types .PhotoStrippedSize ]

class PhotoSize :
    """"""

    QUALNAME ="hisapyro.raw.base.PhotoSize"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/photo-size")
