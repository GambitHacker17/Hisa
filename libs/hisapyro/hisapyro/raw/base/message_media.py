
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

MessageMedia =Union [raw .types .MessageMediaContact ,raw .types .MessageMediaDice ,raw .types .MessageMediaDocument ,raw .types .MessageMediaEmpty ,raw .types .MessageMediaGame ,raw .types .MessageMediaGeo ,raw .types .MessageMediaGeoLive ,raw .types .MessageMediaInvoice ,raw .types .MessageMediaPhoto ,raw .types .MessageMediaPoll ,raw .types .MessageMediaUnsupported ,raw .types .MessageMediaVenue ,raw .types .MessageMediaWebPage ]

class MessageMedia :
    """"""

    QUALNAME ="hisapyro.raw.base.MessageMedia"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/message-media")
