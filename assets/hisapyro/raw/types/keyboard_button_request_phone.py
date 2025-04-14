from io import BytesIO
from hisapyro.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from hisapyro.raw.core import TLObject
from hisapyro import raw
from typing import List, Optional, Any
class KeyboardButtonRequestPhone(TLObject):  
    __slots__: List[str] = ["text"]
    ID = 0xb16a6c29
    QUALNAME = "types.KeyboardButtonRequestPhone"
    def __init__(self, *, text: str) -> None:
        self.text = text  
    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonRequestPhone":
        text = String.read(b)
        return KeyboardButtonRequestPhone(text=text)
    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))
        b.write(String(self.text))
        return b.getvalue()