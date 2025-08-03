
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelAdminLogEventActionSendMessage (TLObject ):
    """"""

    __slots__ :List [str ]=["message"]

    ID =0x278f2868 
    QUALNAME ="types.ChannelAdminLogEventActionSendMessage"

    def __init__ (self ,*,message :"raw.base.Message")->None :
        self .message =message 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelAdminLogEventActionSendMessage":

        message =TLObject .read (b )

        return ChannelAdminLogEventActionSendMessage (message =message )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .message .write ())

        return b .getvalue ()
