
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ReportAntiSpamFalsePositive (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","msg_id"]

    ID =0xa850a693 
    QUALNAME ="functions.channels.ReportAntiSpamFalsePositive"

    def __init__ (self ,*,channel :"raw.base.InputChannel",msg_id :int )->None :
        self .channel =channel 
        self .msg_id =msg_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ReportAntiSpamFalsePositive":

        channel =TLObject .read (b )

        msg_id =Int .read (b )

        return ReportAntiSpamFalsePositive (channel =channel ,msg_id =msg_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .channel .write ())

        b .write (Int (self .msg_id ))

        return b .getvalue ()
