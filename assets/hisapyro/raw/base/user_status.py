
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

UserStatus =Union [raw .types .UserStatusEmpty ,raw .types .UserStatusLastMonth ,raw .types .UserStatusLastWeek ,raw .types .UserStatusOffline ,raw .types .UserStatusOnline ,raw .types .UserStatusRecently ]

class UserStatus :
    """"""

    QUALNAME ="hisapyro.raw.base.UserStatus"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/user-status")
