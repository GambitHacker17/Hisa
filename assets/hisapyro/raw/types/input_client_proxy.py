
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputClientProxy (TLObject ):
    """"""

    __slots__ :List [str ]=["address","port"]

    ID =0x75588b3f 
    QUALNAME ="types.InputClientProxy"

    def __init__ (self ,*,address :str ,port :int )->None :
        self .address =address 
        self .port =port 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputClientProxy":

        address =String .read (b )

        port =Int .read (b )

        return InputClientProxy (address =address ,port =port )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .address ))

        b .write (Int (self .port ))

        return b .getvalue ()
