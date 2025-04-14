from io import BytesIO
from hisapyro.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from hisapyro.raw.core import TLObject
from hisapyro import raw
from typing import List, Optional, Any
class GetReplies(TLObject):  
    __slots__: List[str] = ["peer", "msg_id", "offset_id", "offset_date", "add_offset", "limit", "max_id", "min_id", "hash"]
    ID = 0x22ddd30c
    QUALNAME = "functions.messages.GetReplies"
    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, offset_id: int, offset_date: int, add_offset: int, limit: int, max_id: int, min_id: int, hash: int) -> None:
        self.peer = peer  
        self.msg_id = msg_id  
        self.offset_id = offset_id  
        self.offset_date = offset_date  
        self.add_offset = add_offset  
        self.limit = limit  
        self.max_id = max_id  
        self.min_id = min_id  
        self.hash = hash  
    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetReplies":
        peer = TLObject.read(b)
        msg_id = Int.read(b)
        offset_id = Int.read(b)
        offset_date = Int.read(b)
        add_offset = Int.read(b)
        limit = Int.read(b)
        max_id = Int.read(b)
        min_id = Int.read(b)
        hash = Long.read(b)
        return GetReplies(peer=peer, msg_id=msg_id, offset_id=offset_id, offset_date=offset_date, add_offset=add_offset, limit=limit, max_id=max_id, min_id=min_id, hash=hash)
    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))
        b.write(self.peer.write())
        b.write(Int(self.msg_id))
        b.write(Int(self.offset_id))
        b.write(Int(self.offset_date))
        b.write(Int(self.add_offset))
        b.write(Int(self.limit))
        b.write(Int(self.max_id))
        b.write(Int(self.min_id))
        b.write(Long(self.hash))
        return b.getvalue()