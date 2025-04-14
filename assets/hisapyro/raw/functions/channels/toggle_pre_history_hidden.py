from io import BytesIO
from hisapyro.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from hisapyro.raw.core import TLObject
from hisapyro import raw
from typing import List, Optional, Any
class TogglePreHistoryHidden(TLObject):  
    __slots__: List[str] = ["channel", "enabled"]
    ID = 0xeabbb94c
    QUALNAME = "functions.channels.TogglePreHistoryHidden"
    def __init__(self, *, channel: "raw.base.InputChannel", enabled: bool) -> None:
        self.channel = channel  
        self.enabled = enabled  
    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TogglePreHistoryHidden":
        channel = TLObject.read(b)
        enabled = Bool.read(b)
        return TogglePreHistoryHidden(channel=channel, enabled=enabled)
    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))
        b.write(self.channel.write())
        b.write(Bool(self.enabled))
        return b.getvalue()