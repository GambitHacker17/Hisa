
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateChatParticipants (TLObject ):
    """"""

    __slots__ :List [str ]=["participants"]

    ID =0x7761198 
    QUALNAME ="types.UpdateChatParticipants"

    def __init__ (self ,*,participants :"raw.base.ChatParticipants")->None :
        self .participants =participants 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateChatParticipants":

        participants =TLObject .read (b )

        return UpdateChatParticipants (participants =participants )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .participants .write ())

        return b .getvalue ()
