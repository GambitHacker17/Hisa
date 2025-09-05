
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class WebPagePending (TLObject ):
    """"""

    __slots__ :List [str ]=["id","date"]

    ID =0xc586da1c 
    QUALNAME ="types.WebPagePending"

    def __init__ (self ,*,id :int ,date :int )->None :
        self .id =id 
        self .date =date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"WebPagePending":

        id =Long .read (b )

        date =Int .read (b )

        return WebPagePending (id =id ,date =date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .id ))

        b .write (Int (self .date ))

        return b .getvalue ()
