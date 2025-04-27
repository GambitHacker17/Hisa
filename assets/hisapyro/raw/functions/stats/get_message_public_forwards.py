
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetMessagePublicForwards (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","msg_id","offset_rate","offset_peer","offset_id","limit"]

    ID =0x5630281b 
    QUALNAME ="functions.stats.GetMessagePublicForwards"

    def __init__ (self ,*,channel :"raw.base.InputChannel",msg_id :int ,offset_rate :int ,offset_peer :"raw.base.InputPeer",offset_id :int ,limit :int )->None :
        self .channel =channel 
        self .msg_id =msg_id 
        self .offset_rate =offset_rate 
        self .offset_peer =offset_peer 
        self .offset_id =offset_id 
        self .limit =limit 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetMessagePublicForwards":

        channel =TLObject .read (b )

        msg_id =Int .read (b )

        offset_rate =Int .read (b )

        offset_peer =TLObject .read (b )

        offset_id =Int .read (b )

        limit =Int .read (b )

        return GetMessagePublicForwards (channel =channel ,msg_id =msg_id ,offset_rate =offset_rate ,offset_peer =offset_peer ,offset_id =offset_id ,limit =limit )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .channel .write ())

        b .write (Int (self .msg_id ))

        b .write (Int (self .offset_rate ))

        b .write (self .offset_peer .write ())

        b .write (Int (self .offset_id ))

        b .write (Int (self .limit ))

        return b .getvalue ()
