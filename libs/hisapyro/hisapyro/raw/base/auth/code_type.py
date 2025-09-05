
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

CodeType =Union [raw .types .auth .CodeTypeCall ,raw .types .auth .CodeTypeFlashCall ,raw .types .auth .CodeTypeFragmentSms ,raw .types .auth .CodeTypeMissedCall ,raw .types .auth .CodeTypeSms ]

class CodeType :
    """"""

    QUALNAME ="hisapyro.raw.base.auth.CodeType"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/code-type")
