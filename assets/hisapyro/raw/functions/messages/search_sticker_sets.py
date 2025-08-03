
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SearchStickerSets (TLObject ):
    """"""

    __slots__ :List [str ]=["q","hash","exclude_featured"]

    ID =0x35705b8a 
    QUALNAME ="functions.messages.SearchStickerSets"

    def __init__ (self ,*,q :str ,hash :int ,exclude_featured :Optional [bool ]=None )->None :
        self .q =q 
        self .hash =hash 
        self .exclude_featured =exclude_featured 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SearchStickerSets":

        flags =Int .read (b )

        exclude_featured =True if flags &(1 <<0 )else False 
        q =String .read (b )

        hash =Long .read (b )

        return SearchStickerSets (q =q ,hash =hash ,exclude_featured =exclude_featured )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .exclude_featured else 0 
        b .write (Int (flags ))

        b .write (String (self .q ))

        b .write (Long (self .hash ))

        return b .getvalue ()
