
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class CreateStickerSet (TLObject ):
    """"""

    __slots__ :List [str ]=["user_id","title","short_name","stickers","masks","animated","videos","emojis","text_color","thumb","software"]

    ID =0x9021ab67 
    QUALNAME ="functions.stickers.CreateStickerSet"

    def __init__ (self ,*,user_id :"raw.base.InputUser",title :str ,short_name :str ,stickers :List ["raw.base.InputStickerSetItem"],masks :Optional [bool ]=None ,animated :Optional [bool ]=None ,videos :Optional [bool ]=None ,emojis :Optional [bool ]=None ,text_color :Optional [bool ]=None ,thumb :"raw.base.InputDocument"=None ,software :Optional [str ]=None )->None :
        self .user_id =user_id 
        self .title =title 
        self .short_name =short_name 
        self .stickers =stickers 
        self .masks =masks 
        self .animated =animated 
        self .videos =videos 
        self .emojis =emojis 
        self .text_color =text_color 
        self .thumb =thumb 
        self .software =software 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"CreateStickerSet":

        flags =Int .read (b )

        masks =True if flags &(1 <<0 )else False 
        animated =True if flags &(1 <<1 )else False 
        videos =True if flags &(1 <<4 )else False 
        emojis =True if flags &(1 <<5 )else False 
        text_color =True if flags &(1 <<6 )else False 
        user_id =TLObject .read (b )

        title =String .read (b )

        short_name =String .read (b )

        thumb =TLObject .read (b )if flags &(1 <<2 )else None 

        stickers =TLObject .read (b )

        software =String .read (b )if flags &(1 <<3 )else None 
        return CreateStickerSet (user_id =user_id ,title =title ,short_name =short_name ,stickers =stickers ,masks =masks ,animated =animated ,videos =videos ,emojis =emojis ,text_color =text_color ,thumb =thumb ,software =software )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .masks else 0 
        flags |=(1 <<1 )if self .animated else 0 
        flags |=(1 <<4 )if self .videos else 0 
        flags |=(1 <<5 )if self .emojis else 0 
        flags |=(1 <<6 )if self .text_color else 0 
        flags |=(1 <<2 )if self .thumb is not None else 0 
        flags |=(1 <<3 )if self .software is not None else 0 
        b .write (Int (flags ))

        b .write (self .user_id .write ())

        b .write (String (self .title ))

        b .write (String (self .short_name ))

        if self .thumb is not None :
            b .write (self .thumb .write ())

        b .write (Vector (self .stickers ))

        if self .software is not None :
            b .write (String (self .software ))

        return b .getvalue ()
