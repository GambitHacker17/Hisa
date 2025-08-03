
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetRecentStickers (TLObject ):
    """"""

    __slots__ :List [str ]=["hash","attached"]

    ID =0x9da9403b 
    QUALNAME ="functions.messages.GetRecentStickers"

    def __init__ (self ,*,hash :int ,attached :Optional [bool ]=None )->None :
        self .hash =hash 
        self .attached =attached 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetRecentStickers":

        flags =Int .read (b )

        attached =True if flags &(1 <<0 )else False 
        hash =Long .read (b )

        return GetRecentStickers (hash =hash ,attached =attached )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .attached else 0 
        b .write (Int (flags ))

        b .write (Long (self .hash ))

        return b .getvalue ()
