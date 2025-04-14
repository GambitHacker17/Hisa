from io import BytesIO
from hisapyro.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from hisapyro.raw.core import TLObject
from hisapyro import raw
from typing import List, Optional, Any
class UpdateEditChannelMessage(TLObject):  
    __slots__: List[str] = ["message", "pts", "pts_count"]
    ID = 0x1b3f4df7
    QUALNAME = "types.UpdateEditChannelMessage"
    def __init__(self, *, message: "raw.base.Message", pts: int, pts_count: int) -> None:
        self.message = message  
        self.pts = pts  
        self.pts_count = pts_count  
    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateEditChannelMessage":
        message = TLObject.read(b)
        pts = Int.read(b)
        pts_count = Int.read(b)
        return UpdateEditChannelMessage(message=message, pts=pts, pts_count=pts_count)
    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))
        b.write(self.message.write())
        b.write(Int(self.pts))
        b.write(Int(self.pts_count))
        return b.getvalue()