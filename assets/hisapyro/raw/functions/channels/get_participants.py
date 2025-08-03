
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetParticipants (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","filter","offset","limit","hash"]

    ID =0x77ced9d0 
    QUALNAME ="functions.channels.GetParticipants"

    def __init__ (self ,*,channel :"raw.base.InputChannel",filter :"raw.base.ChannelParticipantsFilter",offset :int ,limit :int ,hash :int )->None :
        self .channel =channel 
        self .filter =filter 
        self .offset =offset 
        self .limit =limit 
        self .hash =hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetParticipants":

        channel =TLObject .read (b )

        filter =TLObject .read (b )

        offset =Int .read (b )

        limit =Int .read (b )

        hash =Long .read (b )

        return GetParticipants (channel =channel ,filter =filter ,offset =offset ,limit =limit ,hash =hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .channel .write ())

        b .write (self .filter .write ())

        b .write (Int (self .offset ))

        b .write (Int (self .limit ))

        b .write (Long (self .hash ))

        return b .getvalue ()
