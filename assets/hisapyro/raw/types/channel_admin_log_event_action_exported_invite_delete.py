
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelAdminLogEventActionExportedInviteDelete (TLObject ):
    """"""

    __slots__ :List [str ]=["invite"]

    ID =0x5a50fca4 
    QUALNAME ="types.ChannelAdminLogEventActionExportedInviteDelete"

    def __init__ (self ,*,invite :"raw.base.ExportedChatInvite")->None :
        self .invite =invite 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelAdminLogEventActionExportedInviteDelete":

        invite =TLObject .read (b )

        return ChannelAdminLogEventActionExportedInviteDelete (invite =invite )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .invite .write ())

        return b .getvalue ()
