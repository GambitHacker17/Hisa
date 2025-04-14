from io import BytesIO
from hisapyro.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from hisapyro.raw.core import TLObject
from hisapyro import raw
from typing import List, Optional, Any
class VideoSizeEmojiMarkup(TLObject):  
    __slots__: List[str] = ["emoji_id", "background_colors"]
    ID = 0xf85c413c
    QUALNAME = "types.VideoSizeEmojiMarkup"
    def __init__(self, *, emoji_id: int, background_colors: List[int]) -> None:
        self.emoji_id = emoji_id  
        self.background_colors = background_colors  
    @staticmethod
    def read(b: BytesIO, *args: Any) -> "VideoSizeEmojiMarkup":
        emoji_id = Long.read(b)
        background_colors = TLObject.read(b, Int)
        return VideoSizeEmojiMarkup(emoji_id=emoji_id, background_colors=background_colors)
    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))
        b.write(Long(self.emoji_id))
        b.write(Vector(self.background_colors, Int))
        return b.getvalue()