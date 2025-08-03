
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GroupCallDiscarded (TLObject ):
    """"""

    __slots__ :List [str ]=["id","access_hash","duration"]

    ID =0x7780bcb4 
    QUALNAME ="types.GroupCallDiscarded"

    def __init__ (self ,*,id :int ,access_hash :int ,duration :int )->None :
        self .id =id 
        self .access_hash =access_hash 
        self .duration =duration 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GroupCallDiscarded":

        id =Long .read (b )

        access_hash =Long .read (b )

        duration =Int .read (b )

        return GroupCallDiscarded (id =id ,access_hash =access_hash ,duration =duration )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .id ))

        b .write (Long (self .access_hash ))

        b .write (Int (self .duration ))

        return b .getvalue ()
