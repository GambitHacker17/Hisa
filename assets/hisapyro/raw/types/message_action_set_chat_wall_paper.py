
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageActionSetChatWallPaper (TLObject ):
    """"""

    __slots__ :List [str ]=["wallpaper"]

    ID =0xbc44a927 
    QUALNAME ="types.MessageActionSetChatWallPaper"

    def __init__ (self ,*,wallpaper :"raw.base.WallPaper")->None :
        self .wallpaper =wallpaper 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageActionSetChatWallPaper":

        wallpaper =TLObject .read (b )

        return MessageActionSetChatWallPaper (wallpaper =wallpaper )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .wallpaper .write ())

        return b .getvalue ()
