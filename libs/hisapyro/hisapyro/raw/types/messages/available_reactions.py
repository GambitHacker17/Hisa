
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AvailableReactions (TLObject ):
    """"""

    __slots__ :List [str ]=["hash","reactions"]

    ID =0x768e3aad 
    QUALNAME ="types.messages.AvailableReactions"

    def __init__ (self ,*,hash :int ,reactions :List ["raw.base.AvailableReaction"])->None :
        self .hash =hash 
        self .reactions =reactions 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AvailableReactions":

        hash =Int .read (b )

        reactions =TLObject .read (b )

        return AvailableReactions (hash =hash ,reactions =reactions )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .hash ))

        b .write (Vector (self .reactions ))

        return b .getvalue ()
