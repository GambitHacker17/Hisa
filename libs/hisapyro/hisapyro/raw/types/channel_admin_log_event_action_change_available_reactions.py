
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelAdminLogEventActionChangeAvailableReactions (TLObject ):
    """"""

    __slots__ :List [str ]=["prev_value","new_value"]

    ID =0xbe4e0ef8 
    QUALNAME ="types.ChannelAdminLogEventActionChangeAvailableReactions"

    def __init__ (self ,*,prev_value :"raw.base.ChatReactions",new_value :"raw.base.ChatReactions")->None :
        self .prev_value =prev_value 
        self .new_value =new_value 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelAdminLogEventActionChangeAvailableReactions":

        prev_value =TLObject .read (b )

        new_value =TLObject .read (b )

        return ChannelAdminLogEventActionChangeAvailableReactions (prev_value =prev_value ,new_value =new_value )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .prev_value .write ())

        b .write (self .new_value .write ())

        return b .getvalue ()
