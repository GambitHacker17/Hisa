
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SetStickers (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","stickerset"]

    ID =0xea8ca4f9 
    QUALNAME ="functions.channels.SetStickers"

    def __init__ (self ,*,channel :"raw.base.InputChannel",stickerset :"raw.base.InputStickerSet")->None :
        self .channel =channel 
        self .stickerset =stickerset 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SetStickers":

        channel =TLObject .read (b )

        stickerset =TLObject .read (b )

        return SetStickers (channel =channel ,stickerset =stickerset )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .channel .write ())

        b .write (self .stickerset .write ())

        return b .getvalue ()
