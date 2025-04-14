from io import BytesIO
from hisapyro.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from hisapyro.raw.core import TLObject
from hisapyro import raw
from typing import List, Optional, Any
class InputBotAppID(TLObject):  
    __slots__: List[str] = ["id", "access_hash"]
    ID = 0xa920bd7a
    QUALNAME = "types.InputBotAppID"
    def __init__(self, *, id: int, access_hash: int) -> None:
        self.id = id  
        self.access_hash = access_hash  
    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBotAppID":
        id = Long.read(b)
        access_hash = Long.read(b)
        return InputBotAppID(id=id, access_hash=access_hash)
    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))
        b.write(Long(self.id))
        b.write(Long(self.access_hash))
        return b.getvalue()