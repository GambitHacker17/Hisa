
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

PasswordKdfAlgo =Union [raw .types .PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow ,raw .types .PasswordKdfAlgoUnknown ]

class PasswordKdfAlgo :
    """"""

    QUALNAME ="hisapyro.raw.base.PasswordKdfAlgo"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/password-kdf-algo")
