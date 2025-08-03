
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EditTitle (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","title"]

    ID =0x566decd0 
    QUALNAME ="functions.channels.EditTitle"

    def __init__ (self ,*,channel :"raw.base.InputChannel",title :str )->None :
        self .channel =channel 
        self .title =title 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EditTitle":

        channel =TLObject .read (b )

        title =String .read (b )

        return EditTitle (channel =channel ,title =title )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .channel .write ())

        b .write (String (self .title ))

        return b .getvalue ()
