from io import BytesIO
from hisapyro.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from hisapyro.raw.core import TLObject
from hisapyro import raw
from typing import List, Optional, Any
class PageRelatedArticle(TLObject):  
    __slots__: List[str] = ["url", "webpage_id", "title", "description", "photo_id", "author", "published_date"]
    ID = 0xb390dc08
    QUALNAME = "types.PageRelatedArticle"
    def __init__(self, *, url: str, webpage_id: int, title: Optional[str] = None, description: Optional[str] = None, photo_id: Optional[int] = None, author: Optional[str] = None, published_date: Optional[int] = None) -> None:
        self.url = url  
        self.webpage_id = webpage_id  
        self.title = title  
        self.description = description  
        self.photo_id = photo_id  
        self.author = author  
        self.published_date = published_date  
    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageRelatedArticle":
        flags = Int.read(b)
        url = String.read(b)
        webpage_id = Long.read(b)
        title = String.read(b) if flags & (1 << 0) else None
        description = String.read(b) if flags & (1 << 1) else None
        photo_id = Long.read(b) if flags & (1 << 2) else None
        author = String.read(b) if flags & (1 << 3) else None
        published_date = Int.read(b) if flags & (1 << 4) else None
        return PageRelatedArticle(url=url, webpage_id=webpage_id, title=title, description=description, photo_id=photo_id, author=author, published_date=published_date)
    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))
        flags = 0
        flags |= (1 << 0) if self.title is not None else 0
        flags |= (1 << 1) if self.description is not None else 0
        flags |= (1 << 2) if self.photo_id is not None else 0
        flags |= (1 << 3) if self.author is not None else 0
        flags |= (1 << 4) if self.published_date is not None else 0
        b.write(Int(flags))
        b.write(String(self.url))
        b.write(Long(self.webpage_id))
        if self.title is not None:
            b.write(String(self.title))
        if self.description is not None:
            b.write(String(self.description))
        if self.photo_id is not None:
            b.write(Long(self.photo_id))
        if self.author is not None:
            b.write(String(self.author))
        if self.published_date is not None:
            b.write(Int(self.published_date))
        return b.getvalue()