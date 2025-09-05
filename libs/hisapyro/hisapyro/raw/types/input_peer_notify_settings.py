
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputPeerNotifySettings (TLObject ):
    """"""

    __slots__ :List [str ]=["show_previews","silent","mute_until","sound"]

    ID =0xdf1f002b 
    QUALNAME ="types.InputPeerNotifySettings"

    def __init__ (self ,*,show_previews :Optional [bool ]=None ,silent :Optional [bool ]=None ,mute_until :Optional [int ]=None ,sound :"raw.base.NotificationSound"=None )->None :
        self .show_previews =show_previews 
        self .silent =silent 
        self .mute_until =mute_until 
        self .sound =sound 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputPeerNotifySettings":

        flags =Int .read (b )

        show_previews =Bool .read (b )if flags &(1 <<0 )else None 
        silent =Bool .read (b )if flags &(1 <<1 )else None 
        mute_until =Int .read (b )if flags &(1 <<2 )else None 
        sound =TLObject .read (b )if flags &(1 <<3 )else None 

        return InputPeerNotifySettings (show_previews =show_previews ,silent =silent ,mute_until =mute_until ,sound =sound )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .show_previews is not None else 0 
        flags |=(1 <<1 )if self .silent is not None else 0 
        flags |=(1 <<2 )if self .mute_until is not None else 0 
        flags |=(1 <<3 )if self .sound is not None else 0 
        b .write (Int (flags ))

        if self .show_previews is not None :
            b .write (Bool (self .show_previews ))

        if self .silent is not None :
            b .write (Bool (self .silent ))

        if self .mute_until is not None :
            b .write (Int (self .mute_until ))

        if self .sound is not None :
            b .write (self .sound .write ())

        return b .getvalue ()
