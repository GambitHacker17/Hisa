
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelAdminLogEventActionDefaultBannedRights (TLObject ):
    """"""

    __slots__ :List [str ]=["prev_banned_rights","new_banned_rights"]

    ID =0x2df5fc0a 
    QUALNAME ="types.ChannelAdminLogEventActionDefaultBannedRights"

    def __init__ (self ,*,prev_banned_rights :"raw.base.ChatBannedRights",new_banned_rights :"raw.base.ChatBannedRights")->None :
        self .prev_banned_rights =prev_banned_rights 
        self .new_banned_rights =new_banned_rights 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelAdminLogEventActionDefaultBannedRights":

        prev_banned_rights =TLObject .read (b )

        new_banned_rights =TLObject .read (b )

        return ChannelAdminLogEventActionDefaultBannedRights (prev_banned_rights =prev_banned_rights ,new_banned_rights =new_banned_rights )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .prev_banned_rights .write ())

        b .write (self .new_banned_rights .write ())

        return b .getvalue ()
