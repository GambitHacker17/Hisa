
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateUsername (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","username"]

    ID =0x3514b3de 
    QUALNAME ="functions.channels.UpdateUsername"

    def __init__ (self ,*,channel :"raw.base.InputChannel",username :str )->None :
        self .channel =channel 
        self .username =username 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateUsername":

        channel =TLObject .read (b )

        username =String .read (b )

        return UpdateUsername (channel =channel ,username =username )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .channel .write ())

        b .write (String (self .username ))

        return b .getvalue ()
