
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelAdminLogEventActionChangeAbout (TLObject ):
    """"""

    __slots__ :List [str ]=["prev_value","new_value"]

    ID =0x55188a2e 
    QUALNAME ="types.ChannelAdminLogEventActionChangeAbout"

    def __init__ (self ,*,prev_value :str ,new_value :str )->None :
        self .prev_value =prev_value 
        self .new_value =new_value 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelAdminLogEventActionChangeAbout":

        prev_value =String .read (b )

        new_value =String .read (b )

        return ChannelAdminLogEventActionChangeAbout (prev_value =prev_value ,new_value =new_value )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .prev_value ))

        b .write (String (self .new_value ))

        return b .getvalue ()
