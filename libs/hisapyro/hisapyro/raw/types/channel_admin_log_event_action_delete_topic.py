
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelAdminLogEventActionDeleteTopic (TLObject ):
    """"""

    __slots__ :List [str ]=["topic"]

    ID =0xae168909 
    QUALNAME ="types.ChannelAdminLogEventActionDeleteTopic"

    def __init__ (self ,*,topic :"raw.base.ForumTopic")->None :
        self .topic =topic 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelAdminLogEventActionDeleteTopic":

        topic =TLObject .read (b )

        return ChannelAdminLogEventActionDeleteTopic (topic =topic )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .topic .write ())

        return b .getvalue ()
