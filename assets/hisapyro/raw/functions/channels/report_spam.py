
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ReportSpam (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","participant","id"]

    ID =0xf44a8315 
    QUALNAME ="functions.channels.ReportSpam"

    def __init__ (self ,*,channel :"raw.base.InputChannel",participant :"raw.base.InputPeer",id :List [int ])->None :
        self .channel =channel 
        self .participant =participant 
        self .id =id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ReportSpam":

        channel =TLObject .read (b )

        participant =TLObject .read (b )

        id =TLObject .read (b ,Int )

        return ReportSpam (channel =channel ,participant =participant ,id =id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .channel .write ())

        b .write (self .participant .write ())

        b .write (Vector (self .id ,Int ))

        return b .getvalue ()
