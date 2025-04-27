
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageActionSetSameChatWallPaper (TLObject ):
    """"""

    __slots__ :List [str ]=["wallpaper"]

    ID =0xc0787d6d 
    QUALNAME ="types.MessageActionSetSameChatWallPaper"

    def __init__ (self ,*,wallpaper :"raw.base.WallPaper")->None :
        self .wallpaper =wallpaper 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageActionSetSameChatWallPaper":

        wallpaper =TLObject .read (b )

        return MessageActionSetSameChatWallPaper (wallpaper =wallpaper )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .wallpaper .write ())

        return b .getvalue ()
