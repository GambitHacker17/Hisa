
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SaveWallPaper (TLObject ):
    """"""

    __slots__ :List [str ]=["wallpaper","unsave","settings"]

    ID =0x6c5a5b37 
    QUALNAME ="functions.account.SaveWallPaper"

    def __init__ (self ,*,wallpaper :"raw.base.InputWallPaper",unsave :bool ,settings :"raw.base.WallPaperSettings")->None :
        self .wallpaper =wallpaper 
        self .unsave =unsave 
        self .settings =settings 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SaveWallPaper":

        wallpaper =TLObject .read (b )

        unsave =Bool .read (b )

        settings =TLObject .read (b )

        return SaveWallPaper (wallpaper =wallpaper ,unsave =unsave ,settings =settings )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .wallpaper .write ())

        b .write (Bool (self .unsave ))

        b .write (self .settings .write ())

        return b .getvalue ()
