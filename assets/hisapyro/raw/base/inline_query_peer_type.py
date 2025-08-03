
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

InlineQueryPeerType =Union [raw .types .InlineQueryPeerTypeBotPM ,raw .types .InlineQueryPeerTypeBroadcast ,raw .types .InlineQueryPeerTypeChat ,raw .types .InlineQueryPeerTypeMegagroup ,raw .types .InlineQueryPeerTypePM ,raw .types .InlineQueryPeerTypeSameBotPM ]

class InlineQueryPeerType :
    """"""

    QUALNAME ="hisapyro.raw.base.InlineQueryPeerType"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/inline-query-peer-type")
