
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetMessages (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","id"]

    ID =0xad8c9a23 
    QUALNAME ="functions.channels.GetMessages"

    def __init__ (self ,*,channel :"raw.base.InputChannel",id :List ["raw.base.InputMessage"])->None :
        self .channel =channel 
        self .id =id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetMessages":

        channel =TLObject .read (b )

        id =TLObject .read (b )

        return GetMessages (channel =channel ,id =id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .channel .write ())

        b .write (Vector (self .id ))

        return b .getvalue ()
