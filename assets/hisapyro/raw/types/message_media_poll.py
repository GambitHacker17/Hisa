
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageMediaPoll (TLObject ):
    """"""

    __slots__ :List [str ]=["poll","results"]

    ID =0x4bd6e798 
    QUALNAME ="types.MessageMediaPoll"

    def __init__ (self ,*,poll :"raw.base.Poll",results :"raw.base.PollResults")->None :
        self .poll =poll 
        self .results =results 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageMediaPoll":

        poll =TLObject .read (b )

        results =TLObject .read (b )

        return MessageMediaPoll (poll =poll ,results =results )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .poll .write ())

        b .write (self .results .write ())

        return b .getvalue ()
