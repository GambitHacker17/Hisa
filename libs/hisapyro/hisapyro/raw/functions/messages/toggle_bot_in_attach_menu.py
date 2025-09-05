
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ToggleBotInAttachMenu (TLObject ):
    """"""

    __slots__ :List [str ]=["bot","enabled","write_allowed"]

    ID =0x69f59d69 
    QUALNAME ="functions.messages.ToggleBotInAttachMenu"

    def __init__ (self ,*,bot :"raw.base.InputUser",enabled :bool ,write_allowed :Optional [bool ]=None )->None :
        self .bot =bot 
        self .enabled =enabled 
        self .write_allowed =write_allowed 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ToggleBotInAttachMenu":

        flags =Int .read (b )

        write_allowed =True if flags &(1 <<0 )else False 
        bot =TLObject .read (b )

        enabled =Bool .read (b )

        return ToggleBotInAttachMenu (bot =bot ,enabled =enabled ,write_allowed =write_allowed )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .write_allowed else 0 
        b .write (Int (flags ))

        b .write (self .bot .write ())

        b .write (Bool (self .enabled ))

        return b .getvalue ()
