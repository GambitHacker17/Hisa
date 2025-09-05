
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InviteToChannel (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","users"]

    ID =0x199f3a6c 
    QUALNAME ="functions.channels.InviteToChannel"

    def __init__ (self ,*,channel :"raw.base.InputChannel",users :List ["raw.base.InputUser"])->None :
        self .channel =channel 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InviteToChannel":

        channel =TLObject .read (b )

        users =TLObject .read (b )

        return InviteToChannel (channel =channel ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .channel .write ())

        b .write (Vector (self .users ))

        return b .getvalue ()
