
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

JSONValue =Union [raw .types .JsonArray ,raw .types .JsonBool ,raw .types .JsonNull ,raw .types .JsonNumber ,raw .types .JsonObject ,raw .types .JsonString ]

class JSONValue :
    """"""

    QUALNAME ="hisapyro.raw.base.JSONValue"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/json-value")
