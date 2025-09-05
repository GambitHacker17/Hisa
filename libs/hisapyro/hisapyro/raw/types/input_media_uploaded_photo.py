
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputMediaUploadedPhoto (TLObject ):
    """"""

    __slots__ :List [str ]=["file","spoiler","stickers","ttl_seconds"]

    ID =0x1e287d04 
    QUALNAME ="types.InputMediaUploadedPhoto"

    def __init__ (self ,*,file :"raw.base.InputFile",spoiler :Optional [bool ]=None ,stickers :Optional [List ["raw.base.InputDocument"]]=None ,ttl_seconds :Optional [int ]=None )->None :
        self .file =file 
        self .spoiler =spoiler 
        self .stickers =stickers 
        self .ttl_seconds =ttl_seconds 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputMediaUploadedPhoto":

        flags =Int .read (b )

        spoiler =True if flags &(1 <<2 )else False 
        file =TLObject .read (b )

        stickers =TLObject .read (b )if flags &(1 <<0 )else []

        ttl_seconds =Int .read (b )if flags &(1 <<1 )else None 
        return InputMediaUploadedPhoto (file =file ,spoiler =spoiler ,stickers =stickers ,ttl_seconds =ttl_seconds )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<2 )if self .spoiler else 0 
        flags |=(1 <<0 )if self .stickers else 0 
        flags |=(1 <<1 )if self .ttl_seconds is not None else 0 
        b .write (Int (flags ))

        b .write (self .file .write ())

        if self .stickers is not None :
            b .write (Vector (self .stickers ))

        if self .ttl_seconds is not None :
            b .write (Int (self .ttl_seconds ))

        return b .getvalue ()
