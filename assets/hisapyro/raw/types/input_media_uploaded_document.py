
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputMediaUploadedDocument (TLObject ):
    """"""

    __slots__ :List [str ]=["file","mime_type","attributes","nosound_video","force_file","spoiler","thumb","stickers","ttl_seconds"]

    ID =0x5b38c6c1 
    QUALNAME ="types.InputMediaUploadedDocument"

    def __init__ (self ,*,file :"raw.base.InputFile",mime_type :str ,attributes :List ["raw.base.DocumentAttribute"],nosound_video :Optional [bool ]=None ,force_file :Optional [bool ]=None ,spoiler :Optional [bool ]=None ,thumb :"raw.base.InputFile"=None ,stickers :Optional [List ["raw.base.InputDocument"]]=None ,ttl_seconds :Optional [int ]=None )->None :
        self .file =file 
        self .mime_type =mime_type 
        self .attributes =attributes 
        self .nosound_video =nosound_video 
        self .force_file =force_file 
        self .spoiler =spoiler 
        self .thumb =thumb 
        self .stickers =stickers 
        self .ttl_seconds =ttl_seconds 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputMediaUploadedDocument":

        flags =Int .read (b )

        nosound_video =True if flags &(1 <<3 )else False 
        force_file =True if flags &(1 <<4 )else False 
        spoiler =True if flags &(1 <<5 )else False 
        file =TLObject .read (b )

        thumb =TLObject .read (b )if flags &(1 <<2 )else None 

        mime_type =String .read (b )

        attributes =TLObject .read (b )

        stickers =TLObject .read (b )if flags &(1 <<0 )else []

        ttl_seconds =Int .read (b )if flags &(1 <<1 )else None 
        return InputMediaUploadedDocument (file =file ,mime_type =mime_type ,attributes =attributes ,nosound_video =nosound_video ,force_file =force_file ,spoiler =spoiler ,thumb =thumb ,stickers =stickers ,ttl_seconds =ttl_seconds )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<3 )if self .nosound_video else 0 
        flags |=(1 <<4 )if self .force_file else 0 
        flags |=(1 <<5 )if self .spoiler else 0 
        flags |=(1 <<2 )if self .thumb is not None else 0 
        flags |=(1 <<0 )if self .stickers else 0 
        flags |=(1 <<1 )if self .ttl_seconds is not None else 0 
        b .write (Int (flags ))

        b .write (self .file .write ())

        if self .thumb is not None :
            b .write (self .thumb .write ())

        b .write (String (self .mime_type ))

        b .write (Vector (self .attributes ))

        if self .stickers is not None :
            b .write (Vector (self .stickers ))

        if self .ttl_seconds is not None :
            b .write (Int (self .ttl_seconds ))

        return b .getvalue ()
