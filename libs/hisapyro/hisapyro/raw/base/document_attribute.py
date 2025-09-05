
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

DocumentAttribute =Union [raw .types .DocumentAttributeAnimated ,raw .types .DocumentAttributeAudio ,raw .types .DocumentAttributeCustomEmoji ,raw .types .DocumentAttributeFilename ,raw .types .DocumentAttributeHasStickers ,raw .types .DocumentAttributeImageSize ,raw .types .DocumentAttributeSticker ,raw .types .DocumentAttributeVideo ]

class DocumentAttribute :
    """"""

    QUALNAME ="hisapyro.raw.base.DocumentAttribute"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/document-attribute")
