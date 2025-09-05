
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelAdminLogEventActionToggleNoForwards (TLObject ):
    """"""

    __slots__ :List [str ]=["new_value"]

    ID =0xcb2ac766 
    QUALNAME ="types.ChannelAdminLogEventActionToggleNoForwards"

    def __init__ (self ,*,new_value :bool )->None :
        self .new_value =new_value 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelAdminLogEventActionToggleNoForwards":

        new_value =Bool .read (b )

        return ChannelAdminLogEventActionToggleNoForwards (new_value =new_value )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Bool (self .new_value ))

        return b .getvalue ()
