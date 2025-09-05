
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class StickerSetInstallResultArchive (TLObject ):
    """"""

    __slots__ :List [str ]=["sets"]

    ID =0x35e410a8 
    QUALNAME ="types.messages.StickerSetInstallResultArchive"

    def __init__ (self ,*,sets :List ["raw.base.StickerSetCovered"])->None :
        self .sets =sets 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"StickerSetInstallResultArchive":

        sets =TLObject .read (b )

        return StickerSetInstallResultArchive (sets =sets )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .sets ))

        return b .getvalue ()
