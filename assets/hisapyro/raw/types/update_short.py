
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateShort (TLObject ):
    """"""

    __slots__ :List [str ]=["update","date"]

    ID =0x78d4dec1 
    QUALNAME ="types.UpdateShort"

    def __init__ (self ,*,update :"raw.base.Update",date :int )->None :
        self .update =update 
        self .date =date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateShort":

        update =TLObject .read (b )

        date =Int .read (b )

        return UpdateShort (update =update ,date =date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .update .write ())

        b .write (Int (self .date ))

        return b .getvalue ()
