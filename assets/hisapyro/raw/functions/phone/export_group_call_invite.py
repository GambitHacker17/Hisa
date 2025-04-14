from io import BytesIO
from hisapyro.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from hisapyro.raw.core import TLObject
from hisapyro import raw
from typing import List, Optional, Any
class ExportGroupCallInvite(TLObject):  
    __slots__: List[str] = ["call", "can_self_unmute"]
    ID = 0xe6aa647f
    QUALNAME = "functions.phone.ExportGroupCallInvite"
    def __init__(self, *, call: "raw.base.InputGroupCall", can_self_unmute: Optional[bool] = None) -> None:
        self.call = call  
        self.can_self_unmute = can_self_unmute  
    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportGroupCallInvite":
        flags = Int.read(b)
        can_self_unmute = True if flags & (1 << 0) else False
        call = TLObject.read(b)
        return ExportGroupCallInvite(call=call, can_self_unmute=can_self_unmute)
    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))
        flags = 0
        flags |= (1 << 0) if self.can_self_unmute else 0
        b.write(Int(flags))
        b.write(self.call.write())
        return b.getvalue()