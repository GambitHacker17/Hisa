
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SaveAppLog (TLObject ):
    """"""

    __slots__ :List [str ]=["events"]

    ID =0x6f02f748 
    QUALNAME ="functions.help.SaveAppLog"

    def __init__ (self ,*,events :List ["raw.base.InputAppEvent"])->None :
        self .events =events 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SaveAppLog":

        events =TLObject .read (b )

        return SaveAppLog (events =events )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .events ))

        return b .getvalue ()
