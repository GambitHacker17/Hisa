
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Chats (TLObject ):
    """"""

    __slots__ :List [str ]=["chats"]

    ID =0x64ff9fd5 
    QUALNAME ="types.messages.Chats"

    def __init__ (self ,*,chats :List ["raw.base.Chat"])->None :
        self .chats =chats 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Chats":

        chats =TLObject .read (b )

        return Chats (chats =chats )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .chats ))

        return b .getvalue ()
