
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SetChatWallPaper (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","wallpaper","settings","id"]

    ID =0x8ffacae1 
    QUALNAME ="functions.messages.SetChatWallPaper"

    def __init__ (self ,*,peer :"raw.base.InputPeer",wallpaper :"raw.base.InputWallPaper"=None ,settings :"raw.base.WallPaperSettings"=None ,id :Optional [int ]=None )->None :
        self .peer =peer 
        self .wallpaper =wallpaper 
        self .settings =settings 
        self .id =id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SetChatWallPaper":

        flags =Int .read (b )

        peer =TLObject .read (b )

        wallpaper =TLObject .read (b )if flags &(1 <<0 )else None 

        settings =TLObject .read (b )if flags &(1 <<2 )else None 

        id =Int .read (b )if flags &(1 <<1 )else None 
        return SetChatWallPaper (peer =peer ,wallpaper =wallpaper ,settings =settings ,id =id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .wallpaper is not None else 0 
        flags |=(1 <<2 )if self .settings is not None else 0 
        flags |=(1 <<1 )if self .id is not None else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        if self .wallpaper is not None :
            b .write (self .wallpaper .write ())

        if self .settings is not None :
            b .write (self .settings .write ())

        if self .id is not None :
            b .write (Int (self .id ))

        return b .getvalue ()
