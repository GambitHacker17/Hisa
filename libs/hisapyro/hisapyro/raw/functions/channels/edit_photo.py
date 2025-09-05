
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EditPhoto (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","photo"]

    ID =0xf12e57c9 
    QUALNAME ="functions.channels.EditPhoto"

    def __init__ (self ,*,channel :"raw.base.InputChannel",photo :"raw.base.InputChatPhoto")->None :
        self .channel =channel 
        self .photo =photo 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EditPhoto":

        channel =TLObject .read (b )

        photo =TLObject .read (b )

        return EditPhoto (channel =channel ,photo =photo )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .channel .write ())

        b .write (self .photo .write ())

        return b .getvalue ()
