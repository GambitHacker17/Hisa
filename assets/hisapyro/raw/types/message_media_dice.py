
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageMediaDice (TLObject ):
    """"""

    __slots__ :List [str ]=["value","emoticon"]

    ID =0x3f7ee58b 
    QUALNAME ="types.MessageMediaDice"

    def __init__ (self ,*,value :int ,emoticon :str )->None :
        self .value =value 
        self .emoticon =emoticon 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageMediaDice":

        value =Int .read (b )

        emoticon =String .read (b )

        return MessageMediaDice (value =value ,emoticon =emoticon )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .value ))

        b .write (String (self .emoticon ))

        return b .getvalue ()
