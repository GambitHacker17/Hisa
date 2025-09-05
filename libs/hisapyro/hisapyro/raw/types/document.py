
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Document (TLObject ):
    """"""

    __slots__ :List [str ]=["id","access_hash","file_reference","date","mime_type","size","dc_id","attributes","thumbs","video_thumbs"]

    ID =0x8fd4c4d8 
    QUALNAME ="types.Document"

    def __init__ (self ,*,id :int ,access_hash :int ,file_reference :bytes ,date :int ,mime_type :str ,size :int ,dc_id :int ,attributes :List ["raw.base.DocumentAttribute"],thumbs :Optional [List ["raw.base.PhotoSize"]]=None ,video_thumbs :Optional [List ["raw.base.VideoSize"]]=None )->None :
        self .id =id 
        self .access_hash =access_hash 
        self .file_reference =file_reference 
        self .date =date 
        self .mime_type =mime_type 
        self .size =size 
        self .dc_id =dc_id 
        self .attributes =attributes 
        self .thumbs =thumbs 
        self .video_thumbs =video_thumbs 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Document":

        flags =Int .read (b )

        id =Long .read (b )

        access_hash =Long .read (b )

        file_reference =Bytes .read (b )

        date =Int .read (b )

        mime_type =String .read (b )

        size =Long .read (b )

        thumbs =TLObject .read (b )if flags &(1 <<0 )else []

        video_thumbs =TLObject .read (b )if flags &(1 <<1 )else []

        dc_id =Int .read (b )

        attributes =TLObject .read (b )

        return Document (id =id ,access_hash =access_hash ,file_reference =file_reference ,date =date ,mime_type =mime_type ,size =size ,dc_id =dc_id ,attributes =attributes ,thumbs =thumbs ,video_thumbs =video_thumbs )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .thumbs else 0 
        flags |=(1 <<1 )if self .video_thumbs else 0 
        b .write (Int (flags ))

        b .write (Long (self .id ))

        b .write (Long (self .access_hash ))

        b .write (Bytes (self .file_reference ))

        b .write (Int (self .date ))

        b .write (String (self .mime_type ))

        b .write (Long (self .size ))

        if self .thumbs is not None :
            b .write (Vector (self .thumbs ))

        if self .video_thumbs is not None :
            b .write (Vector (self .video_thumbs ))

        b .write (Int (self .dc_id ))

        b .write (Vector (self .attributes ))

        return b .getvalue ()
