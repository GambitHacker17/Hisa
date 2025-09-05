
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class TopPeerCategoryBotsPM (TLObject ):
    """"""

    __slots__ :List [str ]=[]

    ID =0xab661b5b 
    QUALNAME ="types.TopPeerCategoryBotsPM"

    def __init__ (self )->None :
        pass 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"TopPeerCategoryBotsPM":

        return TopPeerCategoryBotsPM ()

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        return b .getvalue ()
