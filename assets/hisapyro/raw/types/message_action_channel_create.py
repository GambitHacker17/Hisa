
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageActionChannelCreate (TLObject ):
    """"""

    __slots__ :List [str ]=["title"]

    ID =0x95d2ac92 
    QUALNAME ="types.MessageActionChannelCreate"

    def __init__ (self ,*,title :str )->None :
        self .title =title 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageActionChannelCreate":

        title =String .read (b )

        return MessageActionChannelCreate (title =title )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .title ))

        return b .getvalue ()
