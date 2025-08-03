
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class RecentMeUrlStickerSet (TLObject ):
    """"""

    __slots__ :List [str ]=["url","set"]

    ID =0xbc0a57dc 
    QUALNAME ="types.RecentMeUrlStickerSet"

    def __init__ (self ,*,url :str ,set :"raw.base.StickerSetCovered")->None :
        self .url =url 
        self .set =set 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"RecentMeUrlStickerSet":

        url =String .read (b )

        set =TLObject .read (b )

        return RecentMeUrlStickerSet (url =url ,set =set )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .url ))

        b .write (self .set .write ())

        return b .getvalue ()
