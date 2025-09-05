
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

InputChatPhoto =Union [raw .types .InputChatPhoto ,raw .types .InputChatPhotoEmpty ,raw .types .InputChatUploadedPhoto ]

class InputChatPhoto :
    """"""

    QUALNAME ="hisapyro.raw.base.InputChatPhoto"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/input-chat-photo")
