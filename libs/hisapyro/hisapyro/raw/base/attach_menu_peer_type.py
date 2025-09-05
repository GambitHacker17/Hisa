
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

AttachMenuPeerType =Union [raw .types .AttachMenuPeerTypeBotPM ,raw .types .AttachMenuPeerTypeBroadcast ,raw .types .AttachMenuPeerTypeChat ,raw .types .AttachMenuPeerTypePM ,raw .types .AttachMenuPeerTypeSameBotPM ]

class AttachMenuPeerType :
    """"""

    QUALNAME ="hisapyro.raw.base.AttachMenuPeerType"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/attach-menu-peer-type")
