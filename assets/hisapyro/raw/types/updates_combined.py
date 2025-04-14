from io import BytesIO
from hisapyro.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from hisapyro.raw.core import TLObject
from hisapyro import raw
from typing import List, Optional, Any
class UpdatesCombined(TLObject):  
    __slots__: List[str] = ["updates", "users", "chats", "date", "seq_start", "seq"]
    ID = 0x725b04c3
    QUALNAME = "types.UpdatesCombined"
    def __init__(self, *, updates: List["raw.base.Update"], users: List["raw.base.User"], chats: List["raw.base.Chat"], date: int, seq_start: int, seq: int) -> None:
        self.updates = updates  
        self.users = users  
        self.chats = chats  
        self.date = date  
        self.seq_start = seq_start  
        self.seq = seq  
    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatesCombined":
        updates = TLObject.read(b)
        users = TLObject.read(b)
        chats = TLObject.read(b)
        date = Int.read(b)
        seq_start = Int.read(b)
        seq = Int.read(b)
        return UpdatesCombined(updates=updates, users=users, chats=chats, date=date, seq_start=seq_start, seq=seq)
    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))
        b.write(Vector(self.updates))
        b.write(Vector(self.users))
        b.write(Vector(self.chats))
        b.write(Int(self.date))
        b.write(Int(self.seq_start))
        b.write(Int(self.seq))
        return b.getvalue()