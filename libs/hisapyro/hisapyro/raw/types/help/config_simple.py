
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ConfigSimple (TLObject ):
    """"""

    __slots__ :List [str ]=["date","expires","rules"]

    ID =0x5a592a6c 
    QUALNAME ="types.help.ConfigSimple"

    def __init__ (self ,*,date :int ,expires :int ,rules :List ["raw.base.AccessPointRule"])->None :
        self .date =date 
        self .expires =expires 
        self .rules =rules 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ConfigSimple":

        date =Int .read (b )

        expires =Int .read (b )

        rules =TLObject .read (b )

        return ConfigSimple (date =date ,expires =expires ,rules =rules )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .date ))

        b .write (Int (self .expires ))

        b .write (Vector (self .rules ))

        return b .getvalue ()
