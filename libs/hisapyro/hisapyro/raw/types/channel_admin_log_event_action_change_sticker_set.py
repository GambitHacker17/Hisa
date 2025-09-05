
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelAdminLogEventActionChangeStickerSet (TLObject ):
    """"""

    __slots__ :List [str ]=["prev_stickerset","new_stickerset"]

    ID =0xb1c3caa7 
    QUALNAME ="types.ChannelAdminLogEventActionChangeStickerSet"

    def __init__ (self ,*,prev_stickerset :"raw.base.InputStickerSet",new_stickerset :"raw.base.InputStickerSet")->None :
        self .prev_stickerset =prev_stickerset 
        self .new_stickerset =new_stickerset 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelAdminLogEventActionChangeStickerSet":

        prev_stickerset =TLObject .read (b )

        new_stickerset =TLObject .read (b )

        return ChannelAdminLogEventActionChangeStickerSet (prev_stickerset =prev_stickerset ,new_stickerset =new_stickerset )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .prev_stickerset .write ())

        b .write (self .new_stickerset .write ())

        return b .getvalue ()
