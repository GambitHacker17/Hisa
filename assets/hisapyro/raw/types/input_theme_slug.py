from io import BytesIO
from hisapyro.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from hisapyro.raw.core import TLObject
from hisapyro import raw
from typing import List, Optional, Any
class InputThemeSlug(TLObject):  
    __slots__: List[str] = ["slug"]
    ID = 0xf5890df1
    QUALNAME = "types.InputThemeSlug"
    def __init__(self, *, slug: str) -> None:
        self.slug = slug  
    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputThemeSlug":
        slug = String.read(b)
        return InputThemeSlug(slug=slug)
    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))
        b.write(String(self.slug))
        return b.getvalue()