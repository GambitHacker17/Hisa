from io import BytesIO
from hisapyro.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from hisapyro.raw.core import TLObject
from hisapyro import raw
from typing import List, Optional, Any
class GetMessageEditData(TLObject):  
    __slots__: List[str] = ["peer", "id"]
    ID = 0xfda68d36
    QUALNAME = "functions.messages.GetMessageEditData"
    def __init__(self, *, peer: "raw.base.InputPeer", id: int) -> None:
        self.peer = peer  
        self.id = id  
    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMessageEditData":
        peer = TLObject.read(b)
        id = Int.read(b)
        return GetMessageEditData(peer=peer, id=id)
    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))
        b.write(self.peer.write())
        b.write(Int(self.id))
        return b.getvalue()