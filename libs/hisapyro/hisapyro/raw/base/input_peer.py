
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

InputPeer =Union [raw .types .InputPeerChannel ,raw .types .InputPeerChannelFromMessage ,raw .types .InputPeerChat ,raw .types .InputPeerEmpty ,raw .types .InputPeerSelf ,raw .types .InputPeerUser ,raw .types .InputPeerUserFromMessage ]

class InputPeer :
    """"""

    QUALNAME ="hisapyro.raw.base.InputPeer"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/input-peer")
