
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DeleteChannel (TLObject ):
    """"""

    __slots__ :List [str ]=["channel"]

    ID =0xc0111fe3 
    QUALNAME ="functions.channels.DeleteChannel"

    def __init__ (self ,*,channel :"raw.base.InputChannel")->None :
        self .channel =channel 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DeleteChannel":

        channel =TLObject .read (b )

        return DeleteChannel (channel =channel )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .channel .write ())

        return b .getvalue ()
