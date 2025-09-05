
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ReorderUsernames (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","order"]

    ID =0xb45ced1d 
    QUALNAME ="functions.channels.ReorderUsernames"

    def __init__ (self ,*,channel :"raw.base.InputChannel",order :List [str ])->None :
        self .channel =channel 
        self .order =order 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ReorderUsernames":

        channel =TLObject .read (b )

        order =TLObject .read (b ,String )

        return ReorderUsernames (channel =channel ,order =order )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .channel .write ())

        b .write (Vector (self .order ,String ))

        return b .getvalue ()
