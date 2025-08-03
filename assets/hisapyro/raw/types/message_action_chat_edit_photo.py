
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageActionChatEditPhoto (TLObject ):
    """"""

    __slots__ :List [str ]=["photo"]

    ID =0x7fcb13a8 
    QUALNAME ="types.MessageActionChatEditPhoto"

    def __init__ (self ,*,photo :"raw.base.Photo")->None :
        self .photo =photo 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageActionChatEditPhoto":

        photo =TLObject .read (b )

        return MessageActionChatEditPhoto (photo =photo )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .photo .write ())

        return b .getvalue ()
