
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelAdminLogEventActionParticipantUnmute (TLObject ):
    """"""

    __slots__ :List [str ]=["participant"]

    ID =0xe64429c0 
    QUALNAME ="types.ChannelAdminLogEventActionParticipantUnmute"

    def __init__ (self ,*,participant :"raw.base.GroupCallParticipant")->None :
        self .participant =participant 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelAdminLogEventActionParticipantUnmute":

        participant =TLObject .read (b )

        return ChannelAdminLogEventActionParticipantUnmute (participant =participant )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .participant .write ())

        return b .getvalue ()
