
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ToggleStickerSets (TLObject ):
    """"""

    __slots__ :List [str ]=["stickersets","uninstall","archive","unarchive"]

    ID =0xb5052fea 
    QUALNAME ="functions.messages.ToggleStickerSets"

    def __init__ (self ,*,stickersets :List ["raw.base.InputStickerSet"],uninstall :Optional [bool ]=None ,archive :Optional [bool ]=None ,unarchive :Optional [bool ]=None )->None :
        self .stickersets =stickersets 
        self .uninstall =uninstall 
        self .archive =archive 
        self .unarchive =unarchive 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ToggleStickerSets":

        flags =Int .read (b )

        uninstall =True if flags &(1 <<0 )else False 
        archive =True if flags &(1 <<1 )else False 
        unarchive =True if flags &(1 <<2 )else False 
        stickersets =TLObject .read (b )

        return ToggleStickerSets (stickersets =stickersets ,uninstall =uninstall ,archive =archive ,unarchive =unarchive )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .uninstall else 0 
        flags |=(1 <<1 )if self .archive else 0 
        flags |=(1 <<2 )if self .unarchive else 0 
        b .write (Int (flags ))

        b .write (Vector (self .stickersets ))

        return b .getvalue ()
