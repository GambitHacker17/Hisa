
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateDeleteScheduledMessages (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","messages"]

    ID =0x90866cee 
    QUALNAME ="types.UpdateDeleteScheduledMessages"

    def __init__ (self ,*,peer :"raw.base.Peer",messages :List [int ])->None :
        self .peer =peer 
        self .messages =messages 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateDeleteScheduledMessages":

        peer =TLObject .read (b )

        messages =TLObject .read (b ,Int )

        return UpdateDeleteScheduledMessages (peer =peer ,messages =messages )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Vector (self .messages ,Int ))

        return b .getvalue ()
