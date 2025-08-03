
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelParticipantsContacts (TLObject ):
    """"""

    __slots__ :List [str ]=["q"]

    ID =0xbb6ae88d 
    QUALNAME ="types.ChannelParticipantsContacts"

    def __init__ (self ,*,q :str )->None :
        self .q =q 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelParticipantsContacts":

        q =String .read (b )

        return ChannelParticipantsContacts (q =q )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .q ))

        return b .getvalue ()
