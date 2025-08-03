
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SetEncryptedTyping (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","typing"]

    ID =0x791451ed 
    QUALNAME ="functions.messages.SetEncryptedTyping"

    def __init__ (self ,*,peer :"raw.base.InputEncryptedChat",typing :bool )->None :
        self .peer =peer 
        self .typing =typing 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SetEncryptedTyping":

        peer =TLObject .read (b )

        typing =Bool .read (b )

        return SetEncryptedTyping (peer =peer ,typing =typing )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Bool (self .typing ))

        return b .getvalue ()
