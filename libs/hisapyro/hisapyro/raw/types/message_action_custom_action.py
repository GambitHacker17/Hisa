
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageActionCustomAction (TLObject ):
    """"""

    __slots__ :List [str ]=["message"]

    ID =0xfae69f56 
    QUALNAME ="types.MessageActionCustomAction"

    def __init__ (self ,*,message :str )->None :
        self .message =message 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageActionCustomAction":

        message =String .read (b )

        return MessageActionCustomAction (message =message )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .message ))

        return b .getvalue ()
