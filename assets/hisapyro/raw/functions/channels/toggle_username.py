
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ToggleUsername (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","username","active"]

    ID =0x50f24105 
    QUALNAME ="functions.channels.ToggleUsername"

    def __init__ (self ,*,channel :"raw.base.InputChannel",username :str ,active :bool )->None :
        self .channel =channel 
        self .username =username 
        self .active =active 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ToggleUsername":

        channel =TLObject .read (b )

        username =String .read (b )

        active =Bool .read (b )

        return ToggleUsername (channel =channel ,username =username ,active =active )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .channel .write ())

        b .write (String (self .username ))

        b .write (Bool (self .active ))

        return b .getvalue ()
