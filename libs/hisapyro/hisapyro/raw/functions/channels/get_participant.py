
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetParticipant (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","participant"]

    ID =0xa0ab6cc6 
    QUALNAME ="functions.channels.GetParticipant"

    def __init__ (self ,*,channel :"raw.base.InputChannel",participant :"raw.base.InputPeer")->None :
        self .channel =channel 
        self .participant =participant 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetParticipant":

        channel =TLObject .read (b )

        participant =TLObject .read (b )

        return GetParticipant (channel =channel ,participant =participant )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .channel .write ())

        b .write (self .participant .write ())

        return b .getvalue ()
