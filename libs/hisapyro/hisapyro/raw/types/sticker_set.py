
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class StickerSet (TLObject ):
    """"""

    __slots__ :List [str ]=["id","access_hash","title","short_name","count","hash","archived","official","masks","animated","videos","emojis","installed_date","thumbs","thumb_dc_id","thumb_version","thumb_document_id"]

    ID =0x2dd14edc 
    QUALNAME ="types.StickerSet"

    def __init__ (self ,*,id :int ,access_hash :int ,title :str ,short_name :str ,count :int ,hash :int ,archived :Optional [bool ]=None ,official :Optional [bool ]=None ,masks :Optional [bool ]=None ,animated :Optional [bool ]=None ,videos :Optional [bool ]=None ,emojis :Optional [bool ]=None ,installed_date :Optional [int ]=None ,thumbs :Optional [List ["raw.base.PhotoSize"]]=None ,thumb_dc_id :Optional [int ]=None ,thumb_version :Optional [int ]=None ,thumb_document_id :Optional [int ]=None )->None :
        self .id =id 
        self .access_hash =access_hash 
        self .title =title 
        self .short_name =short_name 
        self .count =count 
        self .hash =hash 
        self .archived =archived 
        self .official =official 
        self .masks =masks 
        self .animated =animated 
        self .videos =videos 
        self .emojis =emojis 
        self .installed_date =installed_date 
        self .thumbs =thumbs 
        self .thumb_dc_id =thumb_dc_id 
        self .thumb_version =thumb_version 
        self .thumb_document_id =thumb_document_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"StickerSet":

        flags =Int .read (b )

        archived =True if flags &(1 <<1 )else False 
        official =True if flags &(1 <<2 )else False 
        masks =True if flags &(1 <<3 )else False 
        animated =True if flags &(1 <<5 )else False 
        videos =True if flags &(1 <<6 )else False 
        emojis =True if flags &(1 <<7 )else False 
        installed_date =Int .read (b )if flags &(1 <<0 )else None 
        id =Long .read (b )

        access_hash =Long .read (b )

        title =String .read (b )

        short_name =String .read (b )

        thumbs =TLObject .read (b )if flags &(1 <<4 )else []

        thumb_dc_id =Int .read (b )if flags &(1 <<4 )else None 
        thumb_version =Int .read (b )if flags &(1 <<4 )else None 
        thumb_document_id =Long .read (b )if flags &(1 <<8 )else None 
        count =Int .read (b )

        hash =Int .read (b )

        return StickerSet (id =id ,access_hash =access_hash ,title =title ,short_name =short_name ,count =count ,hash =hash ,archived =archived ,official =official ,masks =masks ,animated =animated ,videos =videos ,emojis =emojis ,installed_date =installed_date ,thumbs =thumbs ,thumb_dc_id =thumb_dc_id ,thumb_version =thumb_version ,thumb_document_id =thumb_document_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<1 )if self .archived else 0 
        flags |=(1 <<2 )if self .official else 0 
        flags |=(1 <<3 )if self .masks else 0 
        flags |=(1 <<5 )if self .animated else 0 
        flags |=(1 <<6 )if self .videos else 0 
        flags |=(1 <<7 )if self .emojis else 0 
        flags |=(1 <<0 )if self .installed_date is not None else 0 
        flags |=(1 <<4 )if self .thumbs else 0 
        flags |=(1 <<4 )if self .thumb_dc_id is not None else 0 
        flags |=(1 <<4 )if self .thumb_version is not None else 0 
        flags |=(1 <<8 )if self .thumb_document_id is not None else 0 
        b .write (Int (flags ))

        if self .installed_date is not None :
            b .write (Int (self .installed_date ))

        b .write (Long (self .id ))

        b .write (Long (self .access_hash ))

        b .write (String (self .title ))

        b .write (String (self .short_name ))

        if self .thumbs is not None :
            b .write (Vector (self .thumbs ))

        if self .thumb_dc_id is not None :
            b .write (Int (self .thumb_dc_id ))

        if self .thumb_version is not None :
            b .write (Int (self .thumb_version ))

        if self .thumb_document_id is not None :
            b .write (Long (self .thumb_document_id ))

        b .write (Int (self .count ))

        b .write (Int (self .hash ))

        return b .getvalue ()
