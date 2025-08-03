
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateMessagePoll (TLObject ):
    """"""

    __slots__ :List [str ]=["poll_id","results","poll"]

    ID =0xaca1657b 
    QUALNAME ="types.UpdateMessagePoll"

    def __init__ (self ,*,poll_id :int ,results :"raw.base.PollResults",poll :"raw.base.Poll"=None )->None :
        self .poll_id =poll_id 
        self .results =results 
        self .poll =poll 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateMessagePoll":

        flags =Int .read (b )

        poll_id =Long .read (b )

        poll =TLObject .read (b )if flags &(1 <<0 )else None 

        results =TLObject .read (b )

        return UpdateMessagePoll (poll_id =poll_id ,results =results ,poll =poll )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .poll is not None else 0 
        b .write (Int (flags ))

        b .write (Long (self .poll_id ))

        if self .poll is not None :
            b .write (self .poll .write ())

        b .write (self .results .write ())

        return b .getvalue ()
