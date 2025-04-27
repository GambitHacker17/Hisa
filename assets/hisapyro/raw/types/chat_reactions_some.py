
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChatReactionsSome (TLObject ):
    """"""

    __slots__ :List [str ]=["reactions"]

    ID =0x661d4037 
    QUALNAME ="types.ChatReactionsSome"

    def __init__ (self ,*,reactions :List ["raw.base.Reaction"])->None :
        self .reactions =reactions 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChatReactionsSome":

        reactions =TLObject .read (b )

        return ChatReactionsSome (reactions =reactions )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .reactions ))

        return b .getvalue ()
