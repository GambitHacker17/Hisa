
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelAdminLogEventActionExportedInviteRevoke (TLObject ):
    """"""

    __slots__ :List [str ]=["invite"]

    ID =0x410a134e 
    QUALNAME ="types.ChannelAdminLogEventActionExportedInviteRevoke"

    def __init__ (self ,*,invite :"raw.base.ExportedChatInvite")->None :
        self .invite =invite 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelAdminLogEventActionExportedInviteRevoke":

        invite =TLObject .read (b )

        return ChannelAdminLogEventActionExportedInviteRevoke (invite =invite )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .invite .write ())

        return b .getvalue ()
