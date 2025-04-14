from io import BytesIO
from hisapyro.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from hisapyro.raw.core import TLObject
from hisapyro import raw
from typing import List, Optional, Any
class BotInlineMessageMediaVenue(TLObject):  
    __slots__: List[str] = ["geo", "title", "address", "provider", "venue_id", "venue_type", "reply_markup"]
    ID = 0x8a86659c
    QUALNAME = "types.BotInlineMessageMediaVenue"
    def __init__(self, *, geo: "raw.base.GeoPoint", title: str, address: str, provider: str, venue_id: str, venue_type: str, reply_markup: "raw.base.ReplyMarkup" = None) -> None:
        self.geo = geo  
        self.title = title  
        self.address = address  
        self.provider = provider  
        self.venue_id = venue_id  
        self.venue_type = venue_type  
        self.reply_markup = reply_markup  
    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotInlineMessageMediaVenue":
        flags = Int.read(b)
        geo = TLObject.read(b)
        title = String.read(b)
        address = String.read(b)
        provider = String.read(b)
        venue_id = String.read(b)
        venue_type = String.read(b)
        reply_markup = TLObject.read(b) if flags & (1 << 2) else None
        return BotInlineMessageMediaVenue(geo=geo, title=title, address=address, provider=provider, venue_id=venue_id, venue_type=venue_type, reply_markup=reply_markup)
    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))
        flags = 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        b.write(Int(flags))
        b.write(self.geo.write())
        b.write(String(self.title))
        b.write(String(self.address))
        b.write(String(self.provider))
        b.write(String(self.venue_id))
        b.write(String(self.venue_type))
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        return b.getvalue()