
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputStickeredMediaPhoto (TLObject ):
    """"""

    __slots__ :List [str ]=["id"]

    ID =0x4a992157 
    QUALNAME ="types.InputStickeredMediaPhoto"

    def __init__ (self ,*,id :"raw.base.InputPhoto")->None :
        self .id =id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputStickeredMediaPhoto":

        id =TLObject .read (b )

        return InputStickeredMediaPhoto (id =id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .id .write ())

        return b .getvalue ()
