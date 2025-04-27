
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class WallPapers (TLObject ):
    """"""

    __slots__ :List [str ]=["hash","wallpapers"]

    ID =0xcdc3858c 
    QUALNAME ="types.account.WallPapers"

    def __init__ (self ,*,hash :int ,wallpapers :List ["raw.base.WallPaper"])->None :
        self .hash =hash 
        self .wallpapers =wallpapers 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"WallPapers":

        hash =Long .read (b )

        wallpapers =TLObject .read (b )

        return WallPapers (hash =hash ,wallpapers =wallpapers )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .hash ))

        b .write (Vector (self .wallpapers ))

        return b .getvalue ()
