
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AttachMenuBotIconColor (TLObject ):
    """"""

    __slots__ :List [str ]=["name","color"]

    ID =0x4576f3f0 
    QUALNAME ="types.AttachMenuBotIconColor"

    def __init__ (self ,*,name :str ,color :int )->None :
        self .name =name 
        self .color =color 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AttachMenuBotIconColor":

        name =String .read (b )

        color =Int .read (b )

        return AttachMenuBotIconColor (name =name ,color =color )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .name ))

        b .write (Int (self .color ))

        return b .getvalue ()
