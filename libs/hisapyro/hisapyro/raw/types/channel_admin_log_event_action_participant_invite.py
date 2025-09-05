
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelAdminLogEventActionParticipantInvite (TLObject ):
    """"""

    __slots__ :List [str ]=["participant"]

    ID =0xe31c34d8 
    QUALNAME ="types.ChannelAdminLogEventActionParticipantInvite"

    def __init__ (self ,*,participant :"raw.base.ChannelParticipant")->None :
        self .participant =participant 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelAdminLogEventActionParticipantInvite":

        participant =TLObject .read (b )

        return ChannelAdminLogEventActionParticipantInvite (participant =participant )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .participant .write ())

        return b .getvalue ()
