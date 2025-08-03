
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DeactivateAllUsernames (TLObject ):
    """"""

    __slots__ :List [str ]=["channel"]

    ID =0xa245dd3 
    QUALNAME ="functions.channels.DeactivateAllUsernames"

    def __init__ (self ,*,channel :"raw.base.InputChannel")->None :
        self .channel =channel 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DeactivateAllUsernames":

        channel =TLObject .read (b )

        return DeactivateAllUsernames (channel =channel )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .channel .write ())

        return b .getvalue ()
