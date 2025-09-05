
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelAdminLogEventActionChangeUsernames (TLObject ):
    """"""

    __slots__ :List [str ]=["prev_value","new_value"]

    ID =0xf04fb3a9 
    QUALNAME ="types.ChannelAdminLogEventActionChangeUsernames"

    def __init__ (self ,*,prev_value :List [str ],new_value :List [str ])->None :
        self .prev_value =prev_value 
        self .new_value =new_value 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelAdminLogEventActionChangeUsernames":

        prev_value =TLObject .read (b ,String )

        new_value =TLObject .read (b ,String )

        return ChannelAdminLogEventActionChangeUsernames (prev_value =prev_value ,new_value =new_value )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .prev_value ,String ))

        b .write (Vector (self .new_value ,String ))

        return b .getvalue ()
