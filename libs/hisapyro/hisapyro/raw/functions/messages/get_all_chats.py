
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetAllChats (TLObject ):
    """"""

    __slots__ :List [str ]=["except_ids"]

    ID =0x875f74be 
    QUALNAME ="functions.messages.GetAllChats"

    def __init__ (self ,*,except_ids :List [int ])->None :
        self .except_ids =except_ids 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetAllChats":

        except_ids =TLObject .read (b ,Long )

        return GetAllChats (except_ids =except_ids )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .except_ids ,Long ))

        return b .getvalue ()
