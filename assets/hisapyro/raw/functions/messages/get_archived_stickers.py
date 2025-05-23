
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetArchivedStickers (TLObject ):
    """"""

    __slots__ :List [str ]=["offset_id","limit","masks","emojis"]

    ID =0x57f17692 
    QUALNAME ="functions.messages.GetArchivedStickers"

    def __init__ (self ,*,offset_id :int ,limit :int ,masks :Optional [bool ]=None ,emojis :Optional [bool ]=None )->None :
        self .offset_id =offset_id 
        self .limit =limit 
        self .masks =masks 
        self .emojis =emojis 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetArchivedStickers":

        flags =Int .read (b )

        masks =True if flags &(1 <<0 )else False 
        emojis =True if flags &(1 <<1 )else False 
        offset_id =Long .read (b )

        limit =Int .read (b )

        return GetArchivedStickers (offset_id =offset_id ,limit =limit ,masks =masks ,emojis =emojis )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .masks else 0 
        flags |=(1 <<1 )if self .emojis else 0 
        b .write (Int (flags ))

        b .write (Long (self .offset_id ))

        b .write (Int (self .limit ))

        return b .getvalue ()
