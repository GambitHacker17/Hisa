
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

InputFileLocation =Union [raw .types .InputDocumentFileLocation ,raw .types .InputEncryptedFileLocation ,raw .types .InputFileLocation ,raw .types .InputGroupCallStream ,raw .types .InputPeerPhotoFileLocation ,raw .types .InputPhotoFileLocation ,raw .types .InputPhotoLegacyFileLocation ,raw .types .InputSecureFileLocation ,raw .types .InputStickerSetThumb ,raw .types .InputTakeoutFileLocation ]

class InputFileLocation :
    """"""

    QUALNAME ="hisapyro.raw.base.InputFileLocation"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/input-file-location")
