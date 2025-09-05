
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class File (TLObject ):
    """"""

    __slots__ :List [str ]=["type","mtime","bytes"]

    ID =0x96a18d5 
    QUALNAME ="types.upload.File"

    def __init__ (self ,*,type :"raw.base.storage.FileType",mtime :int ,bytes :bytes )->None :
        self .type =type 
        self .mtime =mtime 
        self .bytes =bytes 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"File":

        type =TLObject .read (b )

        mtime =Int .read (b )

        bytes =Bytes .read (b )

        return File (type =type ,mtime =mtime ,bytes =bytes )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .type .write ())

        b .write (Int (self .mtime ))

        b .write (Bytes (self .bytes ))

        return b .getvalue ()
