
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class HttpWait (TLObject ):
    """"""

    __slots__ :List [str ]=["max_delay","wait_after","max_wait"]

    ID =0x9299359f 
    QUALNAME ="types.HttpWait"

    def __init__ (self ,*,max_delay :int ,wait_after :int ,max_wait :int )->None :
        self .max_delay =max_delay 
        self .wait_after =wait_after 
        self .max_wait =max_wait 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"HttpWait":

        max_delay =Int .read (b )

        wait_after =Int .read (b )

        max_wait =Int .read (b )

        return HttpWait (max_delay =max_delay ,wait_after =wait_after ,max_wait =max_wait )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .max_delay ))

        b .write (Int (self .wait_after ))

        b .write (Int (self .max_wait ))

        return b .getvalue ()
