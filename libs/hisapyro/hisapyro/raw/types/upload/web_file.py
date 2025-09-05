
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class WebFile (TLObject ):
    """"""

    __slots__ :List [str ]=["size","mime_type","file_type","mtime","bytes"]

    ID =0x21e753bc 
    QUALNAME ="types.upload.WebFile"

    def __init__ (self ,*,size :int ,mime_type :str ,file_type :"raw.base.storage.FileType",mtime :int ,bytes :bytes )->None :
        self .size =size 
        self .mime_type =mime_type 
        self .file_type =file_type 
        self .mtime =mtime 
        self .bytes =bytes 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"WebFile":

        size =Int .read (b )

        mime_type =String .read (b )

        file_type =TLObject .read (b )

        mtime =Int .read (b )

        bytes =Bytes .read (b )

        return WebFile (size =size ,mime_type =mime_type ,file_type =file_type ,mtime =mtime ,bytes =bytes )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .size ))

        b .write (String (self .mime_type ))

        b .write (self .file_type .write ())

        b .write (Int (self .mtime ))

        b .write (Bytes (self .bytes ))

        return b .getvalue ()
