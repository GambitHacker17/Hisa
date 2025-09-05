
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

NotifyPeer =Union [raw .types .NotifyBroadcasts ,raw .types .NotifyChats ,raw .types .NotifyForumTopic ,raw .types .NotifyPeer ,raw .types .NotifyUsers ]

class NotifyPeer :
    """"""

    QUALNAME ="hisapyro.raw.base.NotifyPeer"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/notify-peer")
