
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelParticipantsBanned (TLObject ):
    """"""

    __slots__ :List [str ]=["q"]

    ID =0x1427a5e1 
    QUALNAME ="types.ChannelParticipantsBanned"

    def __init__ (self ,*,q :str )->None :
        self .q =q 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelParticipantsBanned":

        q =String .read (b )

        return ChannelParticipantsBanned (q =q )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .q ))

        return b .getvalue ()
