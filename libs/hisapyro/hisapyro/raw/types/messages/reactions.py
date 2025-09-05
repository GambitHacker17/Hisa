
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Reactions (TLObject ):
    """"""

    __slots__ :List [str ]=["hash","reactions"]

    ID =0xeafdf716 
    QUALNAME ="types.messages.Reactions"

    def __init__ (self ,*,hash :int ,reactions :List ["raw.base.Reaction"])->None :
        self .hash =hash 
        self .reactions =reactions 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Reactions":

        hash =Long .read (b )

        reactions =TLObject .read (b )

        return Reactions (hash =hash ,reactions =reactions )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .hash ))

        b .write (Vector (self .reactions ))

        return b .getvalue ()
