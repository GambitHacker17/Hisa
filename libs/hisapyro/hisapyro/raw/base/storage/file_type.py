
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

FileType =Union [raw .types .storage .FileGif ,raw .types .storage .FileJpeg ,raw .types .storage .FileMov ,raw .types .storage .FileMp3 ,raw .types .storage .FileMp4 ,raw .types .storage .FilePartial ,raw .types .storage .FilePdf ,raw .types .storage .FilePng ,raw .types .storage .FileUnknown ,raw .types .storage .FileWebp ]

class FileType :
    """"""

    QUALNAME ="hisapyro.raw.base.storage.FileType"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/file-type")
