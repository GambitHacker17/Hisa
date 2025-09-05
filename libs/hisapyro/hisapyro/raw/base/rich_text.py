
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

RichText =Union [raw .types .TextAnchor ,raw .types .TextBold ,raw .types .TextConcat ,raw .types .TextEmail ,raw .types .TextEmpty ,raw .types .TextFixed ,raw .types .TextImage ,raw .types .TextItalic ,raw .types .TextMarked ,raw .types .TextPhone ,raw .types .TextPlain ,raw .types .TextStrike ,raw .types .TextSubscript ,raw .types .TextSuperscript ,raw .types .TextUnderline ,raw .types .TextUrl ]

class RichText :
    """"""

    QUALNAME ="hisapyro.raw.base.RichText"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/rich-text")
