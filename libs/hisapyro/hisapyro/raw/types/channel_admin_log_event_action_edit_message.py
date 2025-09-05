
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelAdminLogEventActionEditMessage (TLObject ):
    """"""

    __slots__ :List [str ]=["prev_message","new_message"]

    ID =0x709b2405 
    QUALNAME ="types.ChannelAdminLogEventActionEditMessage"

    def __init__ (self ,*,prev_message :"raw.base.Message",new_message :"raw.base.Message")->None :
        self .prev_message =prev_message 
        self .new_message =new_message 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelAdminLogEventActionEditMessage":

        prev_message =TLObject .read (b )

        new_message =TLObject .read (b )

        return ChannelAdminLogEventActionEditMessage (prev_message =prev_message ,new_message =new_message )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .prev_message .write ())

        b .write (self .new_message .write ())

        return b .getvalue ()
