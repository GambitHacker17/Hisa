
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessagesNotModified (TLObject ):
    """"""

    __slots__ :List [str ]=["count"]

    ID =0x74535f21 
    QUALNAME ="types.messages.MessagesNotModified"

    def __init__ (self ,*,count :int )->None :
        self .count =count 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessagesNotModified":

        count =Int .read (b )

        return MessagesNotModified (count =count )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .count ))

        return b .getvalue ()
