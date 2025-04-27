
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelAdminLogEventActionParticipantJoinByRequest (TLObject ):
    """"""

    __slots__ :List [str ]=["invite","approved_by"]

    ID =0xafb6144a 
    QUALNAME ="types.ChannelAdminLogEventActionParticipantJoinByRequest"

    def __init__ (self ,*,invite :"raw.base.ExportedChatInvite",approved_by :int )->None :
        self .invite =invite 
        self .approved_by =approved_by 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelAdminLogEventActionParticipantJoinByRequest":

        invite =TLObject .read (b )

        approved_by =Long .read (b )

        return ChannelAdminLogEventActionParticipantJoinByRequest (invite =invite ,approved_by =approved_by )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .invite .write ())

        b .write (Long (self .approved_by ))

        return b .getvalue ()
