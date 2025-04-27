
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DialogsNotModified (TLObject ):
    """"""

    __slots__ :List [str ]=["count"]

    ID =0xf0e3e596 
    QUALNAME ="types.messages.DialogsNotModified"

    def __init__ (self ,*,count :int )->None :
        self .count =count 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DialogsNotModified":

        count =Int .read (b )

        return DialogsNotModified (count =count )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .count ))

        return b .getvalue ()
