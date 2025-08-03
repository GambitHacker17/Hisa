
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateStickerSetsOrder (TLObject ):
    """"""

    __slots__ :List [str ]=["order","masks","emojis"]

    ID =0xbb2d201 
    QUALNAME ="types.UpdateStickerSetsOrder"

    def __init__ (self ,*,order :List [int ],masks :Optional [bool ]=None ,emojis :Optional [bool ]=None )->None :
        self .order =order 
        self .masks =masks 
        self .emojis =emojis 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateStickerSetsOrder":

        flags =Int .read (b )

        masks =True if flags &(1 <<0 )else False 
        emojis =True if flags &(1 <<1 )else False 
        order =TLObject .read (b ,Long )

        return UpdateStickerSetsOrder (order =order ,masks =masks ,emojis =emojis )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .masks else 0 
        flags |=(1 <<1 )if self .emojis else 0 
        b .write (Int (flags ))

        b .write (Vector (self .order ,Long ))

        return b .getvalue ()
