
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelAdminLogEventActionChangePhoto (TLObject ):
    """"""

    __slots__ :List [str ]=["prev_photo","new_photo"]

    ID =0x434bd2af 
    QUALNAME ="types.ChannelAdminLogEventActionChangePhoto"

    def __init__ (self ,*,prev_photo :"raw.base.Photo",new_photo :"raw.base.Photo")->None :
        self .prev_photo =prev_photo 
        self .new_photo =new_photo 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelAdminLogEventActionChangePhoto":

        prev_photo =TLObject .read (b )

        new_photo =TLObject .read (b )

        return ChannelAdminLogEventActionChangePhoto (prev_photo =prev_photo ,new_photo =new_photo )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .prev_photo .write ())

        b .write (self .new_photo .write ())

        return b .getvalue ()
