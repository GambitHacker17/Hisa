
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetScheduledMessages (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","id"]

    ID =0xbdbb0464 
    QUALNAME ="functions.messages.GetScheduledMessages"

    def __init__ (self ,*,peer :"raw.base.InputPeer",id :List [int ])->None :
        self .peer =peer 
        self .id =id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetScheduledMessages":

        peer =TLObject .read (b )

        id =TLObject .read (b ,Int )

        return GetScheduledMessages (peer =peer ,id =id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Vector (self .id ,Int ))

        return b .getvalue ()
