
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

SecureValueError =Union [raw .types .SecureValueError ,raw .types .SecureValueErrorData ,raw .types .SecureValueErrorFile ,raw .types .SecureValueErrorFiles ,raw .types .SecureValueErrorFrontSide ,raw .types .SecureValueErrorReverseSide ,raw .types .SecureValueErrorSelfie ,raw .types .SecureValueErrorTranslationFile ,raw .types .SecureValueErrorTranslationFiles ]

class SecureValueError :
    """"""

    QUALNAME ="hisapyro.raw.base.SecureValueError"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/secure-value-error")
