
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

Messages =Union [raw .types .messages .ChannelMessages ,raw .types .messages .Messages ,raw .types .messages .MessagesNotModified ,raw .types .messages .MessagesSlice ]

class Messages :
    """"""

    QUALNAME ="hisapyro.raw.base.messages.Messages"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/messages")
