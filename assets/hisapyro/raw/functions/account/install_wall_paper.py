
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InstallWallPaper (TLObject ):
    """"""

    __slots__ :List [str ]=["wallpaper","settings"]

    ID =0xfeed5769 
    QUALNAME ="functions.account.InstallWallPaper"

    def __init__ (self ,*,wallpaper :"raw.base.InputWallPaper",settings :"raw.base.WallPaperSettings")->None :
        self .wallpaper =wallpaper 
        self .settings =settings 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InstallWallPaper":

        wallpaper =TLObject .read (b )

        settings =TLObject .read (b )

        return InstallWallPaper (wallpaper =wallpaper ,settings =settings )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .wallpaper .write ())

        b .write (self .settings .write ())

        return b .getvalue ()
