
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ClearRecentStickers (TLObject ):
    """"""

    __slots__ :List [str ]=["attached"]

    ID =0x8999602d 
    QUALNAME ="functions.messages.ClearRecentStickers"

    def __init__ (self ,*,attached :Optional [bool ]=None )->None :
        self .attached =attached 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ClearRecentStickers":

        flags =Int .read (b )

        attached =True if flags &(1 <<0 )else False 
        return ClearRecentStickers (attached =attached )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .attached else 0 
        b .write (Int (flags ))

        return b .getvalue ()
