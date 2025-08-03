
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelAdminLogEventActionStopPoll (TLObject ):
    """"""

    __slots__ :List [str ]=["message"]

    ID =0x8f079643 
    QUALNAME ="types.ChannelAdminLogEventActionStopPoll"

    def __init__ (self ,*,message :"raw.base.Message")->None :
        self .message =message 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelAdminLogEventActionStopPoll":

        message =TLObject .read (b )

        return ChannelAdminLogEventActionStopPoll (message =message )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .message .write ())

        return b .getvalue ()
