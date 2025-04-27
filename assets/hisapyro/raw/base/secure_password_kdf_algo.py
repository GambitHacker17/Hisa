
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

SecurePasswordKdfAlgo =Union [raw .types .SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000 ,raw .types .SecurePasswordKdfAlgoSHA512 ,raw .types .SecurePasswordKdfAlgoUnknown ]

class SecurePasswordKdfAlgo :
    """"""

    QUALNAME ="hisapyro.raw.base.SecurePasswordKdfAlgo"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/secure-password-kdf-algo")
