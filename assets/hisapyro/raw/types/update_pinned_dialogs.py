from io import BytesIO
from hisapyro.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from hisapyro.raw.core import TLObject
from hisapyro import raw
from typing import List, Optional, Any
class UpdatePinnedDialogs(TLObject):  
    __slots__: List[str] = ["folder_id", "order"]
    ID = 0xfa0f3ca2
    QUALNAME = "types.UpdatePinnedDialogs"
    def __init__(self, *, folder_id: Optional[int] = None, order: Optional[List["raw.base.DialogPeer"]] = None) -> None:
        self.folder_id = folder_id  
        self.order = order  
    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePinnedDialogs":
        flags = Int.read(b)
        folder_id = Int.read(b) if flags & (1 << 1) else None
        order = TLObject.read(b) if flags & (1 << 0) else []
        return UpdatePinnedDialogs(folder_id=folder_id, order=order)
    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))
        flags = 0
        flags |= (1 << 1) if self.folder_id is not None else 0
        flags |= (1 << 0) if self.order else 0
        b.write(Int(flags))
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        if self.order is not None:
            b.write(Vector(self.order))
        return b.getvalue()