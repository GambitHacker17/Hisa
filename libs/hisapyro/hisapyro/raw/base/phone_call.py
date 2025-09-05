
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

PhoneCall =Union [raw .types .PhoneCall ,raw .types .PhoneCallAccepted ,raw .types .PhoneCallDiscarded ,raw .types .PhoneCallEmpty ,raw .types .PhoneCallRequested ,raw .types .PhoneCallWaiting ]

class PhoneCall :
    """"""

    QUALNAME ="hisapyro.raw.base.PhoneCall"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/phone-call")
