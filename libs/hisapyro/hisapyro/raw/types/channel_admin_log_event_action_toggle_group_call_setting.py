
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelAdminLogEventActionToggleGroupCallSetting (TLObject ):
    """"""

    __slots__ :List [str ]=["join_muted"]

    ID =0x56d6a247 
    QUALNAME ="types.ChannelAdminLogEventActionToggleGroupCallSetting"

    def __init__ (self ,*,join_muted :bool )->None :
        self .join_muted =join_muted 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelAdminLogEventActionToggleGroupCallSetting":

        join_muted =Bool .read (b )

        return ChannelAdminLogEventActionToggleGroupCallSetting (join_muted =join_muted )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Bool (self .join_muted ))

        return b .getvalue ()
