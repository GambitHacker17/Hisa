from io import BytesIO
from hisapyro.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from hisapyro.raw.core import TLObject
from hisapyro import raw
from typing import List, Optional, Any
class PhoneCallAccepted(TLObject):  
    __slots__: List[str] = ["id", "access_hash", "date", "admin_id", "participant_id", "g_b", "protocol", "video"]
    ID = 0x3660c311
    QUALNAME = "types.PhoneCallAccepted"
    def __init__(self, *, id: int, access_hash: int, date: int, admin_id: int, participant_id: int, g_b: bytes, protocol: "raw.base.PhoneCallProtocol", video: Optional[bool] = None) -> None:
        self.id = id  
        self.access_hash = access_hash  
        self.date = date  
        self.admin_id = admin_id  
        self.participant_id = participant_id  
        self.g_b = g_b  
        self.protocol = protocol  
        self.video = video  
    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhoneCallAccepted":
        flags = Int.read(b)
        video = True if flags & (1 << 6) else False
        id = Long.read(b)
        access_hash = Long.read(b)
        date = Int.read(b)
        admin_id = Long.read(b)
        participant_id = Long.read(b)
        g_b = Bytes.read(b)
        protocol = TLObject.read(b)
        return PhoneCallAccepted(id=id, access_hash=access_hash, date=date, admin_id=admin_id, participant_id=participant_id, g_b=g_b, protocol=protocol, video=video)
    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))
        flags = 0
        flags |= (1 << 6) if self.video else 0
        b.write(Int(flags))
        b.write(Long(self.id))
        b.write(Long(self.access_hash))
        b.write(Int(self.date))
        b.write(Long(self.admin_id))
        b.write(Long(self.participant_id))
        b.write(Bytes(self.g_b))
        b.write(self.protocol.write())
        return b.getvalue()