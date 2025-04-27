
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateGroupCallParticipants (TLObject ):
    """"""

    __slots__ :List [str ]=["call","participants","version"]

    ID =0xf2ebdb4e 
    QUALNAME ="types.UpdateGroupCallParticipants"

    def __init__ (self ,*,call :"raw.base.InputGroupCall",participants :List ["raw.base.GroupCallParticipant"],version :int )->None :
        self .call =call 
        self .participants =participants 
        self .version =version 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateGroupCallParticipants":

        call =TLObject .read (b )

        participants =TLObject .read (b )

        version =Int .read (b )

        return UpdateGroupCallParticipants (call =call ,participants =participants ,version =version )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .call .write ())

        b .write (Vector (self .participants ))

        b .write (Int (self .version ))

        return b .getvalue ()
