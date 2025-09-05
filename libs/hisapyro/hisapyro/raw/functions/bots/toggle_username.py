
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ToggleUsername (TLObject ):
    """"""

    __slots__ :List [str ]=["bot","username","active"]

    ID =0x53ca973 
    QUALNAME ="functions.bots.ToggleUsername"

    def __init__ (self ,*,bot :"raw.base.InputUser",username :str ,active :bool )->None :
        self .bot =bot 
        self .username =username 
        self .active =active 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ToggleUsername":

        bot =TLObject .read (b )

        username =String .read (b )

        active =Bool .read (b )

        return ToggleUsername (bot =bot ,username =username ,active =active )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .bot .write ())

        b .write (String (self .username ))

        b .write (Bool (self .active ))

        return b .getvalue ()
