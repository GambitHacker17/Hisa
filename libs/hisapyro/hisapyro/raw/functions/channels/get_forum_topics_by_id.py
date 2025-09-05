
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetForumTopicsByID (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","topics"]

    ID =0xb0831eb9 
    QUALNAME ="functions.channels.GetForumTopicsByID"

    def __init__ (self ,*,channel :"raw.base.InputChannel",topics :List [int ])->None :
        self .channel =channel 
        self .topics =topics 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetForumTopicsByID":

        channel =TLObject .read (b )

        topics =TLObject .read (b ,Int )

        return GetForumTopicsByID (channel =channel ,topics =topics )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .channel .write ())

        b .write (Vector (self .topics ,Int ))

        return b .getvalue ()
