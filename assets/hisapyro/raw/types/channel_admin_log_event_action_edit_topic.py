
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelAdminLogEventActionEditTopic (TLObject ):
    """"""

    __slots__ :List [str ]=["prev_topic","new_topic"]

    ID =0xf06fe208 
    QUALNAME ="types.ChannelAdminLogEventActionEditTopic"

    def __init__ (self ,*,prev_topic :"raw.base.ForumTopic",new_topic :"raw.base.ForumTopic")->None :
        self .prev_topic =prev_topic 
        self .new_topic =new_topic 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelAdminLogEventActionEditTopic":

        prev_topic =TLObject .read (b )

        new_topic =TLObject .read (b )

        return ChannelAdminLogEventActionEditTopic (prev_topic =prev_topic ,new_topic =new_topic )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .prev_topic .write ())

        b .write (self .new_topic .write ())

        return b .getvalue ()
