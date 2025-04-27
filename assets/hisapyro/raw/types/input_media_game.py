
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputMediaGame (TLObject ):
    """"""

    __slots__ :List [str ]=["id"]

    ID =0xd33f43f3 
    QUALNAME ="types.InputMediaGame"

    def __init__ (self ,*,id :"raw.base.InputGame")->None :
        self .id =id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputMediaGame":

        id =TLObject .read (b )

        return InputMediaGame (id =id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .id .write ())

        return b .getvalue ()
