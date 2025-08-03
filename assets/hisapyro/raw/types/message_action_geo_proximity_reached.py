
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageActionGeoProximityReached (TLObject ):
    """"""

    __slots__ :List [str ]=["from_id","to_id","distance"]

    ID =0x98e0d697 
    QUALNAME ="types.MessageActionGeoProximityReached"

    def __init__ (self ,*,from_id :"raw.base.Peer",to_id :"raw.base.Peer",distance :int )->None :
        self .from_id =from_id 
        self .to_id =to_id 
        self .distance =distance 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageActionGeoProximityReached":

        from_id =TLObject .read (b )

        to_id =TLObject .read (b )

        distance =Int .read (b )

        return MessageActionGeoProximityReached (from_id =from_id ,to_id =to_id ,distance =distance )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .from_id .write ())

        b .write (self .to_id .write ())

        b .write (Int (self .distance ))

        return b .getvalue ()
