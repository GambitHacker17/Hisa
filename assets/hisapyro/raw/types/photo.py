
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Photo (TLObject ):
    """"""

    __slots__ :List [str ]=["id","access_hash","file_reference","date","sizes","dc_id","has_stickers","video_sizes"]

    ID =0xfb197a65 
    QUALNAME ="types.Photo"

    def __init__ (self ,*,id :int ,access_hash :int ,file_reference :bytes ,date :int ,sizes :List ["raw.base.PhotoSize"],dc_id :int ,has_stickers :Optional [bool ]=None ,video_sizes :Optional [List ["raw.base.VideoSize"]]=None )->None :
        self .id =id 
        self .access_hash =access_hash 
        self .file_reference =file_reference 
        self .date =date 
        self .sizes =sizes 
        self .dc_id =dc_id 
        self .has_stickers =has_stickers 
        self .video_sizes =video_sizes 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Photo":

        flags =Int .read (b )

        has_stickers =True if flags &(1 <<0 )else False 
        id =Long .read (b )

        access_hash =Long .read (b )

        file_reference =Bytes .read (b )

        date =Int .read (b )

        sizes =TLObject .read (b )

        video_sizes =TLObject .read (b )if flags &(1 <<1 )else []

        dc_id =Int .read (b )

        return Photo (id =id ,access_hash =access_hash ,file_reference =file_reference ,date =date ,sizes =sizes ,dc_id =dc_id ,has_stickers =has_stickers ,video_sizes =video_sizes )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .has_stickers else 0 
        flags |=(1 <<1 )if self .video_sizes else 0 
        b .write (Int (flags ))

        b .write (Long (self .id ))

        b .write (Long (self .access_hash ))

        b .write (Bytes (self .file_reference ))

        b .write (Int (self .date ))

        b .write (Vector (self .sizes ))

        if self .video_sizes is not None :
            b .write (Vector (self .video_sizes ))

        b .write (Int (self .dc_id ))

        return b .getvalue ()
