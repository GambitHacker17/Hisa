from io import BytesIO
from hisapyro.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from hisapyro.raw.core import TLObject
from hisapyro import raw
from typing import List, Optional, Any
class GetUserPhotos(TLObject):  
    __slots__: List[str] = ["user_id", "offset", "max_id", "limit"]
    ID = 0x91cd32a8
    QUALNAME = "functions.photos.GetUserPhotos"
    def __init__(self, *, user_id: "raw.base.InputUser", offset: int, max_id: int, limit: int) -> None:
        self.user_id = user_id  
        self.offset = offset  
        self.max_id = max_id  
        self.limit = limit  
    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetUserPhotos":
        user_id = TLObject.read(b)
        offset = Int.read(b)
        max_id = Long.read(b)
        limit = Int.read(b)
        return GetUserPhotos(user_id=user_id, offset=offset, max_id=max_id, limit=limit)
    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))
        b.write(self.user_id.write())
        b.write(Int(self.offset))
        b.write(Long(self.max_id))
        b.write(Int(self.limit))
        return b.getvalue()