
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Ping (TLObject ):
    """"""

    __slots__ :List [str ]=["ping_id"]

    ID =0x7abe77ec 
    QUALNAME ="functions.Ping"

    def __init__ (self ,*,ping_id :int )->None :
        self .ping_id =ping_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Ping":

        ping_id =Long .read (b )

        return Ping (ping_id =ping_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .ping_id ))

        return b .getvalue ()
