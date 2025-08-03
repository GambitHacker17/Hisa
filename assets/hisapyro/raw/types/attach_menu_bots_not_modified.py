
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AttachMenuBotsNotModified (TLObject ):
    """"""

    __slots__ :List [str ]=[]

    ID =0xf1d88a5c 
    QUALNAME ="types.AttachMenuBotsNotModified"

    def __init__ (self )->None :
        pass 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AttachMenuBotsNotModified":

        return AttachMenuBotsNotModified ()

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        return b .getvalue ()
