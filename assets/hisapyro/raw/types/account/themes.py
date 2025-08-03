
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Themes (TLObject ):
    """"""

    __slots__ :List [str ]=["hash","themes"]

    ID =0x9a3d8c6d 
    QUALNAME ="types.account.Themes"

    def __init__ (self ,*,hash :int ,themes :List ["raw.base.Theme"])->None :
        self .hash =hash 
        self .themes =themes 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Themes":

        hash =Long .read (b )

        themes =TLObject .read (b )

        return Themes (hash =hash ,themes =themes )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .hash ))

        b .write (Vector (self .themes ))

        return b .getvalue ()
