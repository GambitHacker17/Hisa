
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateStickerSets (TLObject ):
    """"""

    __slots__ :List [str ]=["masks","emojis"]

    ID =0x31c24808 
    QUALNAME ="types.UpdateStickerSets"

    def __init__ (self ,*,masks :Optional [bool ]=None ,emojis :Optional [bool ]=None )->None :
        self .masks =masks 
        self .emojis =emojis 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateStickerSets":

        flags =Int .read (b )

        masks =True if flags &(1 <<0 )else False 
        emojis =True if flags &(1 <<1 )else False 
        return UpdateStickerSets (masks =masks ,emojis =emojis )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .masks else 0 
        flags |=(1 <<1 )if self .emojis else 0 
        b .write (Int (flags ))

        return b .getvalue ()
