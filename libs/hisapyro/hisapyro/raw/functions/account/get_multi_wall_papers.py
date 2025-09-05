
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetMultiWallPapers (TLObject ):
    """"""

    __slots__ :List [str ]=["wallpapers"]

    ID =0x65ad71dc 
    QUALNAME ="functions.account.GetMultiWallPapers"

    def __init__ (self ,*,wallpapers :List ["raw.base.InputWallPaper"])->None :
        self .wallpapers =wallpapers 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetMultiWallPapers":

        wallpapers =TLObject .read (b )

        return GetMultiWallPapers (wallpapers =wallpapers )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .wallpapers ))

        return b .getvalue ()
