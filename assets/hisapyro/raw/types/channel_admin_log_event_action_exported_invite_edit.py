
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelAdminLogEventActionExportedInviteEdit (TLObject ):
    """"""

    __slots__ :List [str ]=["prev_invite","new_invite"]

    ID =0xe90ebb59 
    QUALNAME ="types.ChannelAdminLogEventActionExportedInviteEdit"

    def __init__ (self ,*,prev_invite :"raw.base.ExportedChatInvite",new_invite :"raw.base.ExportedChatInvite")->None :
        self .prev_invite =prev_invite 
        self .new_invite =new_invite 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelAdminLogEventActionExportedInviteEdit":

        prev_invite =TLObject .read (b )

        new_invite =TLObject .read (b )

        return ChannelAdminLogEventActionExportedInviteEdit (prev_invite =prev_invite ,new_invite =new_invite )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .prev_invite .write ())

        b .write (self .new_invite .write ())

        return b .getvalue ()
