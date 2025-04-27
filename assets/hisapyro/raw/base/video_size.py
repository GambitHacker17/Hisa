
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

VideoSize =Union [raw .types .VideoSize ,raw .types .VideoSizeEmojiMarkup ,raw .types .VideoSizeStickerMarkup ]

class VideoSize :
    """"""

    QUALNAME ="hisapyro.raw.base.VideoSize"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/video-size")
