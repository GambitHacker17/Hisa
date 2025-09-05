
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelAdminLogEventActionChangeLinkedChat (TLObject ):
    """"""

    __slots__ :List [str ]=["prev_value","new_value"]

    ID =0x50c7ac8 
    QUALNAME ="types.ChannelAdminLogEventActionChangeLinkedChat"

    def __init__ (self ,*,prev_value :int ,new_value :int )->None :
        self .prev_value =prev_value 
        self .new_value =new_value 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelAdminLogEventActionChangeLinkedChat":

        prev_value =Long .read (b )

        new_value =Long .read (b )

        return ChannelAdminLogEventActionChangeLinkedChat (prev_value =prev_value ,new_value =new_value )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .prev_value ))

        b .write (Long (self .new_value ))

        return b .getvalue ()
