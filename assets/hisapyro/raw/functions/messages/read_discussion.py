from io import BytesIO
from hisapyro.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from hisapyro.raw.core import TLObject
from hisapyro import raw
from typing import List, Optional, Any
class ReadDiscussion(TLObject):  
    __slots__: List[str] = ["peer", "msg_id", "read_max_id"]
    ID = 0xf731a9f4
    QUALNAME = "functions.messages.ReadDiscussion"
    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, read_max_id: int) -> None:
        self.peer = peer  
        self.msg_id = msg_id  
        self.read_max_id = read_max_id  
    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReadDiscussion":
        peer = TLObject.read(b)
        msg_id = Int.read(b)
        read_max_id = Int.read(b)
        return ReadDiscussion(peer=peer, msg_id=msg_id, read_max_id=read_max_id)
    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))
        b.write(self.peer.write())
        b.write(Int(self.msg_id))
        b.write(Int(self.read_max_id))
        return b.getvalue()