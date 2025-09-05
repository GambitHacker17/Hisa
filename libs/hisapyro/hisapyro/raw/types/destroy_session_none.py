
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DestroySessionNone (TLObject ):
    """"""

    __slots__ :List [str ]=["session_id"]

    ID =0x62d350c9 
    QUALNAME ="types.DestroySessionNone"

    def __init__ (self ,*,session_id :int )->None :
        self .session_id =session_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DestroySessionNone":

        session_id =Long .read (b )

        return DestroySessionNone (session_id =session_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .session_id ))

        return b .getvalue ()
