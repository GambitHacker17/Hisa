
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputFileBig (TLObject ):
    """"""

    __slots__ :List [str ]=["id","parts","name"]

    ID =0xfa4f0bb5 
    QUALNAME ="types.InputFileBig"

    def __init__ (self ,*,id :int ,parts :int ,name :str )->None :
        self .id =id 
        self .parts =parts 
        self .name =name 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputFileBig":

        id =Long .read (b )

        parts =Int .read (b )

        name =String .read (b )

        return InputFileBig (id =id ,parts =parts ,name =name )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .id ))

        b .write (Int (self .parts ))

        b .write (String (self .name ))

        return b .getvalue ()
