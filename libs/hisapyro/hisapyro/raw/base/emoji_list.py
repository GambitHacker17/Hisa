
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

EmojiList =Union [raw .types .EmojiList ,raw .types .EmojiListNotModified ]

class EmojiList :
    """"""

    QUALNAME ="hisapyro.raw.base.EmojiList"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/emoji-list")
